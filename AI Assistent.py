from tkinter import *
from PIL import Image, ImageTk
import Speech_Ai_ass
import action_AI_ass

root = Tk()

root.title("AI Assistent")
root.geometry("550x690")
root.resizable(False,False)
root.config(bg="#cce8e7")

def ask():
    askval = Speech_Ai_ass.stt()
    actval = action_AI_ass.act(askval)
    text.insert(END,'user--->'+askval+"\n")
    if actval != None:
        text.insert(END,'Bot <---'+str(actval)+"\n")
    if actval == "ok sir thank you":
        root.destroy()

def send():
    send = ent.get()
    bot = action_AI_ass.act(send)
    text.insert(END,'user--->'+send+"\n")
    if bot != None:
        text.insert(END,'Bot <---'+str(bot)+"\n")
    if bot == "ok sir thank you":
        root.destroy()

def dele():
    text.delete("1.0","end")

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#5ab0ac")
frame.grid(row=0, column=1, padx=55, pady=10)

txt  = Label(frame, text="Mithilesh's AI Assistent", font=("times new roman",14, "bold"),bg="#5ab0ac",fg="white")
txt.grid(row=0, column=0, padx=20, pady=10)

image = ImageTk.PhotoImage(Image.open("assitant.png"))
imagelb = Label(frame, image=image)
imagelb.grid(row=1, column=0, pady=20)



text = Text(root, font= ("courier 10 bold"),bg="#f2fafa")
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100)

ent = Entry(root,justify=CENTER)
ent.place(x=100, y=500, width=375, height=30)

btn1 = Button(root, text="ASK", bg="#5ab0ac", padx=40, pady=16, borderwidth=3, relief=SOLID, command=ask)
btn1.place(x=70, y=565)

btn2 = Button(root, text="SEND", bg="#5ab0ac", padx=40, pady=16, borderwidth=3, relief=SOLID, command=send)
btn2.place(x=400, y=565)

btn3 = Button(root, text="DELETE", bg="#5ab0ac", padx=40, pady=16, borderwidth=3, relief=SOLID, command=dele)
btn3.place(x=225, y=565)







root.mainloop()