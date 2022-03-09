import os
import PySimpleGUI as sg
from time import sleep as slp

sg.theme('Reddit')

def inputTimeWindow():
  layout = [
    [sg.Text('>>> DESLIGAMENTO PROGRAMADO <<<')],
    [sg.Text(' ')],
    [sg.Text('Em quanto tempo o PC deve ser desligado?\nInsira o valor em minutos:')],
    [sg.Input(key='timeToShutdown')],
    [sg.Button('Desligar')]
  ]
  mainWindow = sg.Window('Desligamento Automático', layout=layout, finalize=True)

  return mainWindow
    
def abortWindow():
  layout = [
    [sg.Text('Deseja Abortar?')],
    [sg.Button('Sim'), sg.Button('Não')]
  ]

  abortShutdownWindow = sg.Window('Abortar', layout=layout, finalize=True)
  return abortShutdownWindow

def getTimeTinputinSeconds(timeInSeconds):

  convertedTime = int(timeInSeconds) * 60

  slp(3)
  print(f'O computador irá se desligar em {convertedTime} segundos')
  # os.system(f'shutdown /s /t {convertedTime}')
  os.system(f'shutdown /s /t {convertedTime}')

firstWindow, secondWindow = inputTimeWindow(), None

def abortQuestion():
    return os.system("shutdown /a")

while True:
  window, event, values = sg.read_all_windows()
  if window == firstWindow and event == sg.WIN_CLOSED:
    break

  if window == firstWindow and event == 'Desligar':
    getTimeTinputinSeconds(values['timeToShutdown'])
    secondWindow = abortWindow()
    firstWindow.hide()

  if window == secondWindow and event == sg.WIN_CLOSED:
    break

  if window == secondWindow and event == 'Sim':
    abortQuestion()
    secondWindow.close()

  if window == secondWindow and event == 'Não':
    secondWindow.close()
