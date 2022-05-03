from email.message import Message
from playsound import playsound   
import gtts
from gtts import gTTS
import tkinter as tk
converter = tk.Tk()
converter.geometry("500x300")
l1 = tk.Label(text="Enter your text")
l1.grid(row=2, column=1)
msg = tk.StringVar()
e1 = tk.Entry(converter,textvariable=msg, width = 50)#your message will be entered here
e1.grid(row=2,column=5)

def play():
    Mesg = e1.get()
    #Message variable stores the value of entry_field
    tts = gTTS(Mesg, lang='en', tld='co.in', slow=False)
    tts.save('audio.mp3') #saving our audio file
    playsound('audio.mp3')#playing audio file
    
def exit():
    converter.destroy()#calling the exit function i.e converter.minloop
def reset():
    msg.set("")#reseet it for next entry
b1 = tk.Button(converter,background = "blue" ,activebackground="green",command=play,text="play", width = 40)#button for play
b2 = tk.Button(converter,background = "blue", activebackground="green",command=exit, text="exit", width = 40)#button for exit
b3 = tk.Button(converter,background = "blue", activebackground="green",command=reset, text="reset", width = 40)#button for pause
b1.grid(row =8, column=5)
b2.grid(row =10, column=5)
b3.grid(row =12, column=5)
converter.mainloop()
