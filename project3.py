from gtts import gTTS
from playsound import playsound

audio = "speech.mp3"
language = "en"

sp = gTTS(text="enter your text which u want to convert into audio file", lang=language, slow=False)

sp.save(audio)
playsound(audio)




