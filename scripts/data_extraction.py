import fitz  
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = " ".join([para.get_text() for para in paragraphs])
    return text

def get_youtube_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([t['text'] for t in transcript_list])
        return transcript
    except TranscriptsDisabled:
        print(f"Subtitles are disabled for the video ID: {video_id}. Skipping transcript extraction.")
        return ""


if __name__ == "__main__":
    
    pdf_text = extract_text_from_pdf("data/Apple_Vision_Pro_Privacy_Overview.pdf")
    with open("data_extracted/pdf_text.txt", "w", encoding="utf-8") as f:
        f.write(pdf_text)

    
    website_text = scrape_website("https://www.apple.com/apple-vision-pro/")
    with open("data_extracted/website_text.txt", "w", encoding="utf-8") as f:
        f.write(website_text)

    
    youtube_transcript = get_youtube_transcript("TX9qSaGXFyg")  
    with open("data_extracted/youtube_transcript.txt", "w", encoding="utf-8") as f:
        f.write(youtube_transcript)
