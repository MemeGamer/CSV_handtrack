from gtts import gTTS
import os
from playsound import playsound
import time
from datetime import datetime
language = 'en'

def text_to_speech(Detection):
    if Detection!="Hand":
        # print(cTime)
        output = gTTS(text=Detection, lang=language, slow=False)
        output.save("output.mp3")
        playsound('output.mp3')
        time.sleep(1)
        os.remove("output.mp3")