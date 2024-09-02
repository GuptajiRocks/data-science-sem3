import speech_recognition as sr
import requests
from PIL import Image
from io import BytesIO

UNSPLASH_ACCESS_KEY = 'ZRUKcJ5rT6YL0Gm8hWJ9b5oTZc5jhsdu4jx7CMDWXq0'

def listen_to_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the recognition service.")
            return None

def search_image(query):
    search_url = f"https://api.unsplash.com/search/photos"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {"query": query, "per_page": 1}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    if search_results["results"]:
        image_url = search_results["results"][0]["urls"]["regular"]
        return image_url
    else:
        print("No images found.")
        return None

def display_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()

def main():
    
    prompt = listen_to_voice()

    if prompt:
        
        image_url = search_image(prompt)
        
        if image_url:
            
            display_image(image_url)

if __name__ == "__main__":
    main()