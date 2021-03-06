from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition
import threading


data_list=[ 'What is the capital of India',
            'Delhi is the capital of India',
            'In which language you talk',
            'I mostly talk in english',
            'What you do in free time',
            'I memorize things in my free time',
            'Ok bye',
            'bye take care'

            ]

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

# for files in os.listdir('data/data/spanish/'):
#     data = open('data/data/spanish/'+files, 'r', encoding='utf-8').readlines()
trainer.train(data_list)

def botReply():
    question = questionField.get()
    question = question.capitalize()
    answer = bot.get_response(question)
    textarea.insert(END, 'You: ' + question + '\n\n')
    textarea.insert(END, 'Bot: ' + str(answer) + '\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0, END)

def audioToText():
    while True:
        sr = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m, duration=0.2)
                audio = sr.listen(m)
                query = sr.recognize_google(audio)

                questionField.delete(0,END)
                questionField.insert(0, query)
                botReply()
        except Exception as e:
            print(e)

root = Tk()
root.geometry('600x650+100+30')
root.title('ChatBot')
root.config(bg='seashell4')

logopic = PhotoImage(file='pic.png')

logopicLabel = Label(root, image=logopic, bg='seashell4')
logopicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)


questionField = Entry(root, font=('times new roman', 20, 'bold'))
questionField.pack(pady=15, fill=X)

askpic = PhotoImage(file='ask.png')
askbutton = Button(root, image=askpic, bg='seashell4', command=botReply)
askbutton.pack()

def click(event):
    askbutton.invoke()

root.bind('<Return>', click)

thread = threading.Thread(target=audioToText)
thread.setDaemon(True)
thread.start()

root.mainloop()