# YOUTUBE_KEY
from dotenv import load_dotenv
import os
import googleapiclient.discovery
import pandas as pd
# import graph

# Loading YouTube key from .env
load_dotenv()  # Load variables from .env into environment
api_key = os.environ.get('YOUTUBE_KEY')

# Initialize youtube api
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)


def get_statistics(video_id):

    # Retrieve video statistics using the video ID
    response = youtube.videos().list(
        part="statistics,snippet",
        id=video_id
    ).execute()

    channel_id = response['items'][0]['snippet'].get('channelId', None)
    channel_name = response['items'][0]['snippet'].get('channelTitle', "")
    video_name = response['items'][0]['snippet'].get('title', "")
    view_count = response['items'][0]['statistics'].get('viewCount', 0)
    like_count = response['items'][0]['statistics'].get('likeCount', 0)
    comment_count = response['items'][0]['statistics'].get('commentCount', 0)
    # print(response['items'][0]['snippet']['publishedAt'])
    published_at = response['items'][0]['snippet']['publishedAt']
    thumbnail = response['items'][0]['snippet']['thumbnails']['high']['url']  # "width": 480, "height": 360

    # Create a dictionary to store the video statistics
    video_dict = {
        "channel_id": channel_id,
        "channel_name": channel_name,
        "video_name": video_name,
        "view_count": view_count,
        "like_count": like_count,
        "comment_count": comment_count,
        "published_at": published_at,
        "thumbnail": thumbnail
    }

    return video_dict


def get_comments(video_id):
    """Gets comments for a given video ID."""

    comments = []
    next_page_token = None
    comment_count = 0

    while True:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=100
        )
        print(comment_count+100)
        response = request.execute()

        for comment_thread in response.get("items", []):
            comment_snippet = comment_thread.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
            author_name = comment_snippet.get("authorDisplayName", "Unknown Author")
            comment_text = comment_snippet.get("textOriginal", "")
            published_at = comment_snippet.get("publishedAt", "")
            comment_likes = comment_snippet.get("likeCount", 0)
            no_of_replies = comment_thread.get("snippet", {}).get("totalReplyCount", 0)

            comment_info = {
                "author_name": author_name,
                "comment": comment_text,
                "date": published_at,
                "time": published_at if published_at else "",
                "comment_likes": comment_likes,
                "no_of_replies": no_of_replies,
                "reply": []  # Initialize reply as an empty list
            }

            # if no_of_replies > 0:
            #     reply_request = youtube.comments().list(
            #         part="snippet",
            #         parentId=comment_thread["id"],
            #         maxResults=100
            #     )
            #     reply_response = reply_request.execute()
            #     for reply in reply_response.get("items", []):
            #         reply_snippet = reply.get("snippet", {})
            #         reply_text = reply_snippet.get("textOriginal", "")
            #         comment_info["reply"].append(reply_text)

            comments.append(comment_info)
            comment_count += 1
            if comment_count >= 1000:
                return pd.DataFrame(comments)

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break  # No more pages to retrieve

    return pd.DataFrame(comments)


if __name__ == '__main__':
    dict_video = get_statistics("ACPGAnn0m6k")
    for i in dict_video:
        print(i, dict_video[i])

    df = get_comments("ACPGAnn0m6k")
    graph.plot_comments(df)
    # df.to_csv("comments.csv", index=False)

