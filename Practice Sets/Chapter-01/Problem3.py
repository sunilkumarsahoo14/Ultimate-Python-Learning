#Install an external module and use it to perform an operation of your interest.

# I want to convert text to speach so import the module by (pip install pyttsx)
import pyttsx3
engine = pyttsx3.init()
engine.say("Hey Sunil, Good Morning.")
engine.runAndWait()
