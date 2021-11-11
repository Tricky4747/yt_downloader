from pytube import YouTube
import os
import PySimpleGUI as sg

path = os.path.expanduser("~")

sg.theme('BlueMono')   
layout = [  [sg.Text('Youtube Downloader')],
            [sg.Text('Enter the video url'), sg.InputText()],
            [sg.Text('Video will be saved in Videos folder')],
            [sg.Button('Ok'), sg.Button('Exit')]
        ]

window = sg.Window('yt_downloader', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        url = values[0]
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(path + "\\Videos")
        layout.insert(3, "[sg.Text('Done!')]")

window.close()

