import subprocess
import json
#from youtube_transcript_api import YouTubeTranscriptApi
from prompts import example
import requests
from  openai_interactions import return_clips, return_article


def create_chapters(video_id):
    transcript_dict = YouTubeTranscriptApi.get_transcript(video_id) 
    combined_text = ' '.join([f"{entry['text']} [{entry['start']}]" for entry in transcript_dict])
    print(return_clips(example))
    

def get_youtube_chapters(video_id): #if there  are  preexisting chapters like 3B1B
    try:
        # Run the JavaScript file with Node.js
        result = subprocess.run(
            ["node", "get_youtube_chapters.js", video_id],
            capture_output=True,
            text=True,
            check=True
        )

        # Parse the JSON output
        chapters = json.loads(result.stdout)
        return chapters

    except subprocess.CalledProcessError as e:
        print("Error fetching chapters:", e.stderr)
        return None
    
def gen_article(transcript_dict, title, description, start, end):
    texts_in_interval = [entry['text'] for entry in transcript_dict if start <= entry['start'] <= end]
    joined_text = " ".join(texts_in_interval)
    print(joined_text,title,description)
    res = return_article(title,description,joined_text)



    
    
    



# Example usage
# chapters = get_youtube_chapters("aircAruvnKk")
# print(chapters)

res = return_clips(example)
print(res)
first_chapter = res[0][0]
title = first_chapter["title"]
description = first_chapter['description']
start = first_chapter['start_time']
end = first_chapter['end_time']
print(title,description,start,end)

gen_article({},title,description,start,end)
