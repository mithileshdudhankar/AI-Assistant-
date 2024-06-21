import speech_recognition as sr

def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        vd = ""
        try:
            vd = r.recognize_google(audio)
            print(vd)
            return vd
        
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError:
            print("Request Error")
       

