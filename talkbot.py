import pyttsx3
talkbot = pyttsx3.init()
voices = talkbot.getProperty('voices')
talkbot.setProperty('voice', voices[1].id)
talkbot.setProperty("rate", 175)
speech = input("say this: ")
talkbot.say(speech)
talkbot.runAndWait()
print("Program Ended")
