import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

""" 
Future code with paid feature add The Best APIs & Tools.
Later Use openai and gtts to get better output of questions and 
get the google text to speach features - with google cloud subscriptions.
Also install pip install pygames to play mp3 formats in gtts

"""

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Your News Api Key Here"

# Making a speak function to speek the words
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Process command function
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/sunilkumarsahoo14/")
    elif "open silicon" in c.lower():
        webbrowser.open("https://www.silicon.ac.in")
    elif "open blogger" in c.lower():
        webbrowser.open("https://www.blogger.com")
    elif "open typing" in c.lower():
        webbrowser.open("https://www.typingclub.com/sportal/.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/sunilkumar143sibu")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the json response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI Handel the request
        # ---> I will develop this functionality later...(Because It Is Paid!)
        speak("I Can Not Process, Please Fix The Error Inside Me!")


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen to the word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()

        # Recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))