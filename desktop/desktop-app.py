import PySimpleGUI as sg
import subprocess
import os
import time
import sys
import threading
import queue
from enum import Enum
import requests

sg.theme('DarkBrown4')

def main():

    gui_queue = queue.Queue()

    layout = [
        [sg.Image(r'C:\Users\guilh\Documents\dev\memories-overflow\desktop\images\topo_logo2.png')],
        #[sg.Text('Diretório de saída:', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
        #[sg.Text('Endereço alternativo:', size=(15, 1)) ,sg.InputText()],
        [sg.Output(size=(110,30), background_color='black', text_color='white')],
        [sg.Button('Enviar'), sg.Button('Sair')],
        [sg.Text('github.com/guilhermemaas/memories-overflow')],
        #[sg.Text('unifique.com.br')]
    ]

    window = sg.Window('Memories: Overflow', layout)

    while True:        
        event, values = window.read(timeout=15)

        #out_dir = values[1].replace('/', '\\')

        if event == 'Enviar':
            print('Hello Fantasy World!')
            
        try:
            message = gui_queue.get_nowait()    # see if something has been posted to Queue
        except queue.Empty:                     # get_nowait() will get exception when Queue is empty
            message = None                      # nothing in queue so do nothing

        # if message received from queue, then some work was completed
        if message is not None:
            print(message)

            window.refresh()
            
        if event in (None, 'Sair'):
            break

    window.close()

main()