from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def analysis(df):

    key = "871423458701473dbd26b0b89ecc4358"
    endpoint = "https://sentimentcomment.cognitiveservices.azure.com/"

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    documents = df[0:10]
    response = text_analytics_client.analyze_sentiment(documents=documents)

    positive = 0
    negative = 0
    neutral = 0
    p_score = 0
    n_score = 0
    ne_score = 0

    for i in range(len(df)//10):
        documents = df[i*10:(i+1)*10]
        response = text_analytics_client.analyze_sentiment(documents=documents)

        for document in response:
            # print("Document Sentiment: {}".format(document.sentiment))
            if document.sentiment == "positive":
                positive += 1
            elif document.sentiment == "negative":
                negative += 1
            else:
                neutral += 1
            
            p_score += document.confidence_scores.positive
            n_score += document.confidence_scores.negative
            ne_score += document.confidence_scores.neutral


    return positive, negative, neutral, p_score/len(df), n_score/len(df), ne_score/len(df)



if __name__ == "__main__":
    df = ['Sir please upload more video with real numerical questions for interview', "Your videos and your explanations are so good I can't what to attend your love classes thank you", 'The Best Teacher', 'Thanks for the video. But sorry to say that you skipped something. You told Tutorial 13 in this play list you will show how to convert power law distribution to normal distribution in python. How about that', 'Hi krish sir, you were suppose to create a video on box cox transformation', 'Salute sir ❤.', 'Can you tell me the software you are using to write?', 'Kindly, Make part 2 & 3. Thanks', 'Next part of this video??', 'The way you explained this confusing topic, i found that your confidence interval is 99.99% . So we accept our Null Hypothesis Ho based all the evidences given in the video which is given as :\nHo : Krish is the best teacher. 😅', 'Dude, please complete the series.', 'Super', 'Very good video , understood the concept easily .. Thank you.', 'Thank you brother❤ 🔥.', 'Hi you lei almost every video. Most of the time you tell that you are going to make a video like peroto plot with python but you do not make. Please 🥺 do this. It a complaint towards you :(', 'Thank you si r👍 for clearing the concept.', 'Next please exam is going to happen', 'Sir please upload more lectures of ML', 'Is this playlist complete?', 'Brother, there are no further videos of Pareto distribution in the playlist.', 'Will you please upload the basal correction video with mathematical explanation', 'Krish waitying for next videos in same playlist.', 'Waiting for next episodes of this course....', 'How many vedios of stats would come further?', 'Sir please upload next videos', 'Please upload box cox translation practical video krish sir', 'I am from Bangladesh . U have such great quality . Krish please upload the next video asap.', 'Sir, you have not uploaded the entire material yet.', 'Sir please upload the video recording p value', 'Sir next video please', 'Sir please complete the playlist as soon as possible sir please 🙏🙏🙏🙏🙏', 'Sir please complete the playlist as soon as possible sir please 🙏🙏🙏🙏🙏', 'Please deploy end to end data science project', "You don't put too many videos on this channel.", 'Thank you so much dear sir', '❤️❤️💕💕', 'Thank you Krish for this video this would definitely help me a lot', 'Thanks sir you are great', 'After long time finally video on statistics', 'Nice video Krish!\n\nA small clarification for your viewers, we never say: "Accept the null hypothesis"\nWe should rather say "fail to reject".\n\nThe sample test is not evidence proving the null.\nThe sample test should always be considered as evidence disproving the null.\nIf the sample test result is strong enough, then we are successful in disproving the null, "Reject the null hypothesis".\nIf the sample test result is not strong enough, then we have not been successful in disproving the null, "fail to reject the null hypothesis".\n\nAn analogy can be:\n\nHo: Krish is innocent\nH1: Krish is guilty\n\nSample test: Compare krish\'s fingerprints with fingerprints found on crime scene\n\nIf fingerprints match, we have strong evidence from sample test that krish was on crime scene, so we "reject the null that he is innocent"\n\nHowever, if fingerprints do not match, we do not have strong evidence that krish was on crime scene, so we "fail to reject null that he is innocent"\n\nHere, again, we do not know that he is actually innocent. Our test does not prove his innocence. Our test is just not strong enough to prove that he is guilty. (Who knows he may have worn gloves :))', 'Do you have any plans to make video on Estimation & Maximum Likelihood Estimation in detail?', 'Long time to wait for continuing statistics thanks sr']
    print(len(df))
    print(analysis(df))