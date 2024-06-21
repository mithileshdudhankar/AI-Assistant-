import Text_to_speech_AI_asss
import Speech_Ai_ass
import datetime
import webbrowser

def act(user):


    if "what is your name" in user:
        Text_to_speech_AI_asss.tts(" sir My name is Virtual Assistent")
        return "My name is Virtual Assistent"

    elif "what is my name" in user:
        Text_to_speech_AI_asss.tts("sir Your name is mithilesh dudhankar")
        return "Your name is Mithilesh Dudhankar sir"
    
    elif "hello assistant" in user:
        Text_to_speech_AI_asss.tts("Hello sir how can i help you ?")
        return "Hello sir how can i help you ?"

    elif "good morning" in  user:
        Text_to_speech_AI_asss.tts("Good morning sir, wish you a great day ahead ")
        return "Good morning sir, wish you a great day ahead "

    elif "what is the time now" in user:
        ct = datetime.datetime.now()
        time = (str)(ct)+ "Hour: ",(str)(ct.minute)+"Minute"
        Text_to_speech_AI_asss.tts(time)
        return time
    
    elif "shutdown" in user:
        Text_to_speech_AI_asss.tts("ok sir thank you")
        return "ok sir thank you"

    elif "open YouTube" in user:
        webbrowser.open("https://www.youtube.com/")
        Text_to_speech_AI_asss.tts("Youtube is open for you sir")
        return "Youtube is open for you sir"

    elif "open Google" in user:
        webbrowser.open("https://g.co/kgs/XnE4Ctu")
        Text_to_speech_AI_asss.tts("Google is open for you sir")
        return "Google is open for you sir"

    elif "open Netflix" in user:
        webbrowser.open("https://www.netflix.com/")
        Text_to_speech_AI_asss.tts("netflix is open for you sir")
        return "netflix is open for you sir"

    elif "what is the temperature of Nagpur" in user:
            Text_to_speech_AI_asss.tts("The tempreture is 35 degree celsius in nagpur sir")
            return "The tempreture is 35 degree celsius in nagpur sir"

    else:
        Text_to_speech_AI_asss.tts("sorry sir i am not able to understand")
        return "sorry sir i am not able to understand"
