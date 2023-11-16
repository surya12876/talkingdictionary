from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
def search():
    data=json.load(open('data.json'))
    word=enter.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        text.delete(1.0,END)
        for item in meaning:
            text.insert(END,item+'\n\n')
    elif len(get_close_matches(word ,data.keys())) > 0:
        
        closematch=get_close_matches(word,data.keys())[0]
        res= messagebox.askyesno('confirm', 'did you mean\t'+closematch)
        if res==True:
            enter.delete(0,END)
            enter.insert(END,closematch)
            meaning=data[closematch]
            text.delete(1.0,END)
            for item in meaning:
                text.insert(END,item+'\n\n')
        else:
            messagebox.showerror("error",'word does not exist please check it')
            enter.delete(0,END)
            text.delete(1.0,END)
    else:
        messagebox.showinfo('information','word does not exist')
        enter.delete(0,END)
        text.delete(1.0,END)
def clear():
    enter.delete(0,END)
    text.delete(1.0,END)
def exit():
    res=messagebox.askyesno('confirm', 'Are you sure you want to exit')
    if res==True:
        root.destroy()
    else:
        pass
def wordaudio():
    engine.say(enter.get())
    engine.runAndWait()
def meanaudio():
    engine.say(text.get(1.0,END))
    engine.runAndWait()
          
root=Tk()
root.geometry('1000x676+100+30')
root.title('voicedictionary')
root.resizable(0,0)
bgimg=PhotoImage(file='bg.png')
bg_label = Label(root,image=bgimg )
bg_label.place(x=0,y=0)
word=Label(root,text='ENTER WORD',font=('arial',30,'bold'),foreground='purple',background='whitesmoke')
word.place(x=530,y=30)
enter=Entry(root,font=('arail' ,23, 'italic'),justify='center',bd=7,relief=GROOVE)
enter.place(x=510.5,y=80)
searchimg=PhotoImage(file='searching.png')
searchbutton=Button(root,image=searchimg,bd=0 ,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=search)
searchbutton.place(x=600,y=140)
micimg=PhotoImage(file='microphone2.png')

micbutton=Button(root,image=micimg,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=wordaudio)
micbutton.place(x=700,y=140)

wordmeaning=Label(root,text='MEANING',font=('arial',30,'bold'),foreground='purple',background='whitesmoke')
wordmeaning.place(x=530,y=250)
text=Text(root, width=46,height=8,font=('arial',15),bd=5)
text.place(x=460,y=300)
audioimg= PhotoImage(file='microphone2.png')
audiobutton=Button(root,image=audioimg,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=meanaudio)
audiobutton.place(x=500,y=540)
clearimg= PhotoImage(file='clear.png')
clearbutton=Button(root,image=clearimg,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=clear)
clearbutton.place(x=650,y=540)
exitimg= PhotoImage(file='exit.png')
exitbutton=Button(root,image=exitimg,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=exit)
exitbutton.place(x=800,y=540)
def function(event):
    searchbutton.invoke()

root.bind('<Return>',function)

root.mainloop()
