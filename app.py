from flask import Flask, render_template,request
from modules import comment, graph, get_id, HtoHE, textAnalysis, wordcloud_comment
import json
import datetime 
import pandas as pd
import matplotlib.pyplot as plt
import os
from io import BytesIO
import base64

app = Flask(__name__)




# Define a custom filter function
def format_datetime(value, format='%B %d, %Y at %I:%M %p'):
    try:
        date = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
        return date.strftime(format)
    except ValueError:
        return ''

# Register the filter function in your Flask app
app.jinja_env.filters['formatdatetime'] = format_datetime


def generate_graph(df):
    graph_all, graph_last_7_days = graph.plot_comments(df)
    cloud = wordcloud_comment.create_wordcloud(df['comment'])
    
    # Save the Matplotlib plots as images
    output_dir = 'static/images'  # Define a directory to save the images
    os.makedirs(output_dir, exist_ok=True)

    graph_all_path = os.path.join(output_dir, 'graph_all.png')
    graph_last_7_days_path = os.path.join(output_dir, 'graph_last_7_days.png')
    cloud_path = os.path.join(output_dir, 'wordcloud.png')

    with open(graph_all_path, 'wb') as f1:
        f1.write(base64.b64decode(graph_all))

    with open(graph_last_7_days_path, 'wb') as f2:
        f2.write(base64.b64decode(graph_last_7_days))

    with open(cloud_path, 'wb') as f2:
        f2.write(base64.b64decode(cloud))
    
    return graph_all_path, graph_last_7_days_path, cloud_path




@app.route("/")
def home():
    return render_template("index.html", graph=None)

@app.route('/', methods=['POST'])
def analyze_video():
    youtube_link = request.form.get('youtube-link')
    is_valid, video_id = get_id.validate_and_extract_video_id(youtube_link)
    if is_valid:
        df = comment.get_comments(video_id)
        statistics = comment.get_statistics(video_id)
        translate_df = HtoHE.translate(df)
        positive, negative, neutral, p_score, n_score, ne_score = textAnalysis.analysis(translate_df)
        textData = {
            "positive": positive,
            "negative": negative,
            "neutral": neutral,
            "p_score": p_score,
            "n_score": n_score,
            "ne_score": ne_score
        }
        # print(textData)

        graph_all, graph_last_7_days , cloud = generate_graph(df)
        
        return render_template('index.html' ,
                                graph=graph_all,graph_7 =graph_last_7_days,
                                statistics=statistics, video_id = video_id,
                                cloud=cloud,textData = textData ,error=False)

    else:
        return render_template('index.html', error=True, graph=None)

@app.route("/test", methods=['POST','GET'])
def test():
    return render_template('index_text.html')


    

@app.route("/youtube/<id>")
def youtube(id):
    return comment.get_statistics(id)

@app.route("/graph/<id>")
def graphplot(id):
    df = comment.get_comments(id)
    df.to_csv('comments.csv', index=False)
    return "done"

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)


# Configure static files
app.static_folder = 'static'