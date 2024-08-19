from types import resolve_bases
import speech_recognition as sr
from googletrans import Translator

translator=Translator()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said in Hindi : {}".format(text))
        result=translator.translate(text,src='hi',dest='en')
        print('Your Result in English:{}'.format(result.text))
    except:
        print("Sorry could not recognize what you said")


# from googletrans import Translator

# translator = Translator()
# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

# print(result.src)
# print(result.dest)
# print(result.text)