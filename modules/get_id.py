import re

def validate_and_extract_video_id(link):
    # Define a regular expression pattern to validate YouTube video links
    youtube_url_pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})$')

    # Check if the link matches the pattern
    match = youtube_url_pattern.match(link)
    
    if match:
        video_id = match.group(4)  # Extract the video ID
        return True, video_id
    else:
        return False, None

if __name__=="__main__":

    user_input = input("Enter a YouTube video link: ")

    is_valid, video_id = validate_and_extract_video_id(user_input)

    if is_valid:
        print(f"Valid YouTube link. Video ID: {video_id}")
    else:
        print("Not a valid YouTube video link or video ID length is not 11.")
