from gtts import gTTS
import os

text= "Rock is the best music type in the world"
language ='en'
abc=open("C:\python temelleri\Python\projects\sample.text")
text=abc.read()
obj=gTTS(text=text, lang=language,slow= False)
obj.save("sample.mp3")
os.system("sample.mp3")