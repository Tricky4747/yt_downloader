from pytube import YouTube
import os
import PySimpleGUI as sg

path = os.path.expanduser("~")
sg.ChangeLookAndFeel('black')
sg.theme('DarkBlue12')
layout = [  [sg.Text('Youtube Downloader')],
            [sg.Text('Enter the video url'), sg.InputText()],
            [sg.Text(':)', key='done')],
            [sg.Button('Start'), sg.Button('Exit')]
        ]
window = sg.Window('yt_downloader', layout, icon='./yt.ico')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Start':
        url = values[0]
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(path + "\\Videos")
        window['done'].update('Done!')

window.close()

