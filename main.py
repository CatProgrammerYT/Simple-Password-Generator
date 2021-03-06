
import PySimpleGUI as psg
import time
import pyperclip as pc
import random
from config import *


version = '0.1.1'
themes = psg.theme_list()

layout = [  
            [psg.Text('Current version of app is:'), psg.Text(version)],
            [psg.Text('Please enter here word, which according to something, you cannot forget:')],
            [psg.Text('', size=(15, 1)), psg.InputText()],
            [psg.Button('Generate Random Password')],
            [psg.Submit('Generate')]
        ]

window = psg.Window('Simple Password Generator - Create password you cannot forget!', size=(480, 240)).Layout(layout)
event, values = window.read() 
window.close() 

psg.theme('DarkGrey11')


def generatePassword(password):
    password = password.lower()
    for i in password:
        if i == ' ':
            password = password.replace(i, '')
        if i == 'i':
            password = password.replace(i, '!')
        elif i == 'o':
            password = password.replace(i, '0')
        elif i == 'e':
            password = password.replace(i, '3')
        elif i == 'і' or i == "l":
            password = password.replace(i, '1')
        elif i == 'a':
            password = password.replace(i, '4')
        elif i == 'g':
            password = password.replace(i, '6')
        elif i == 's':
            password = password.replace(i, '5')
    return password

def main():
    if event == "Generate Random Password":
        randpass = random.choice(passWords)
        randpass = randpass.lower()
        randpass = generatePassword(password = randpass)
        psg.Popup(randpass)
        psg.Popup('Successfully copied to clipboard!')
        pc.copy(randpass)
        window.close()
    elif event == 'Generate':
        passWord = values[0]
        passWord = passWord.lower()
        if len(passWord) >= 8:
            finalPass = generatePassword(password = passWord)
            psg.Popup(finalPass)
            psg.Popup('Successfully copied to clipboard!')
            pc.copy(finalPass)
            window.close()
        elif len(passWord) < 8:
            psg.PopupError('Password needs to be longer than 8 symbols!', keep_on_top=True)


main()
