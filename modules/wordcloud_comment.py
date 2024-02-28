import matplotlib.pyplot as plt
from wordcloud import WordCloud
from io import BytesIO
import base64

comments = ['Sir please upload more video with real numerical questions for interview', "Your videos and your explanations are so good I can't what to attend your love classes thank you", 'The Best Teacher', 'Thanks for the video. But sorry to say that you skipped something. You told Tutorial 13 in this play list you will show how to convert power law distribution to normal distribution in python. How about that', 'Hi krish sir, you were suppose to create a video on box cox transformation', 'Salute sir ❤.', 'Can you tell me the software you are using to write?', 'Kindly, Make part 2 & 3. Thanks', 'Next part of this video??', 'The way you explained this confusing topic, i found that your confidence interval is 99.99% . So we accept our Null Hypothesis Ho based all the evidences given in the video which is given as :\nHo : Krish is the best teacher. 😅', 'Dude, please complete the series.', 'Super', 'Very good video , understood the concept easily .. Thank you.', 'Thank you brother❤ 🔥.', 'Hi you lei almost every video. Most of the time you tell that you are going to make a video like peroto plot with python but you do not make. Please 🥺 do this. It a complaint towards you :(', 'Thank you si r👍 for clearing the concept.', 'Next please exam is going to happen', 'Sir please upload more lectures of ML', 'Is this playlist complete?', 'Brother, there are no further videos of Pareto distribution in the playlist.', 'Will you please upload the basal correction video with mathematical explanation', 'Krish waitying for next videos in same playlist.', 'Waiting for next episodes of this course....', 'How many vedios of stats would come further?', 'Sir please upload next videos', 'Please upload box cox translation practical video krish sir', 'I am from Bangladesh . U have such great quality . Krish please upload the next video asap.', 'Sir, you have not uploaded the entire material yet.', 'Sir please upload the video recording p value', 'Sir next video please', 'Sir please complete the playlist as soon as possible sir please 🙏🙏🙏🙏🙏', 'Sir please complete the playlist as soon as possible sir please 🙏🙏🙏🙏🙏', 'Please deploy end to end data science project', "You don't put too many videos on this channel.", 'Thank you so much dear sir', '❤️❤️💕💕', 'Thank you Krish for this video this would definitely help me a lot', 'Thanks sir you are great', 'After long time finally video on statistics', 'Nice video Krish!\n\nA small clarification for your viewers, we never say: "Accept the null hypothesis"\nWe should rather say "fail to reject".\n\nThe sample test is not evidence proving the null.\nThe sample test should always be considered as evidence disproving the null.\nIf the sample test result is strong enough, then we are successful in disproving the null, "Reject the null hypothesis".\nIf the sample test result is not strong enough, then we have not been successful in disproving the null, "fail to reject the null hypothesis".\n\nAn analogy can be:\n\nHo: Krish is innocent\nH1: Krish is guilty\n\nSample test: Compare krish\'s fingerprints with fingerprints found on crime scene\n\nIf fingerprints match, we have strong evidence from sample test that krish was on crime scene, so we "reject the null that he is innocent"\n\nHowever, if fingerprints do not match, we do not have strong evidence that krish was on crime scene, so we "fail to reject null that he is innocent"\n\nHere, again, we do not know that he is actually innocent. Our test does not prove his innocence. Our test is just not strong enough to prove that he is guilty. (Who knows he may have worn gloves :))', 'Do you have any plans to make video on Estimation & Maximum Likelihood Estimation in detail?', 'Long time to wait for continuing statistics thanks sr']

def create_wordcloud(comments):
    # Preprocessing (you can customize this as needed)
    def preprocess_comment(comment):
        comment = comment.lower()  # Convert to lowercase
        # Other preprocessing steps, such as removing punctuation, stopwords, etc.
        return comment

    comments = [preprocess_comment(comment) for comment in comments]


    # Combine comments into a single string
    text = " ".join(comments)

    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=1)

    # Save the graph as a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the BytesIO object in base64
    cloud = base64.b64encode(buffer.read()).decode()

    return cloud
