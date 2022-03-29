import os
import PySimpleGUI as sg

class ScheduledShutdown():
  def __init__(self):
    sg.theme('Reddit')

    layout = [
      [sg.Text('>>> DESLIGAMENTO PROGRAMADO <<<')],
      [sg.Text(' ')],
      [sg.Text('Em quanto tempo o PC deve ser desligado?\nInsira o valor em minutos:')],
      [sg.Input(key='timeToShutdown', size=(40,5))],
      [sg.Button('Desligar')],
      [sg.HorizontalSeparator()],
      [sg.Multiline(key='Log'+sg.WRITE_ONLY_KEY, size=(40,5), disabled = True, no_scrollbar = True)],
      [sg.Button('Abortar Desligamento')]
    ]
    self.mainWindow = sg.Window('Desligamento Automático', layout=layout, finalize=True, icon='.\public\icons\icon.ico')
    self.mainWindow.set_icon(icon='.\public\icons\icon.ico')

  def startApp(self):
    while True:
      self.event, self.values = self.mainWindow.read()

      if self.event == sg.WINDOW_CLOSED:
        break

      if self.event == 'Desligar':
        shut = int(self.values['timeToShutdown'])
        self.getTimeInputinSeconds(shut)
        self.mainWindow['Log'+sg.WRITE_ONLY_KEY].print(f'O computador irá se desligar em {shut*60} segundos')

      if self.event == 'Abortar Desligamento':
        self.mainWindow['Log'+sg.WRITE_ONLY_KEY].print(f'Desligamento cancelado!', text_color='red')
        self.abortShutdown()

    
  def getTimeInputinSeconds(self, timeInMinutes):

    timeInSeconds = timeInMinutes * 60
    os.system(f'shutdown /s /t {timeInSeconds}')
    #print(f'shutdown /s /t {timeInSeconds}')

  def abortShutdown(self):
    return os.system("shutdown /a")

shutdown = ScheduledShutdown()
shutdown.startApp()