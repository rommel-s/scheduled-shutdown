import os
import PySimpleGUI as sg

class ScheduledShutdown():
  def __init__(self):
    sg.theme('Reddit')

    layout = [
      [sg.Text('    DESLIGAMENTO PROGRAMADO    ')],
      [sg.Text(' ')],
      [sg.Text('Em quanto tempo o PC deve ser desligado?')],
      [sg.Input(key='timeToShutdown', size=(40,5))],
      [sg.Text(' ')],
      [sg.Text('Que medida de tempo devo usar?')],
      [sg.Radio('Minutos     ', "RADIO1", key='timeInMinutes', default=True, size=(10,1)), sg.Radio('Horas', "RADIO1", key='timeInHours', size=(10,1))],
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
        self.checkAmountOfTime(shut)

      if self.event == 'Abortar Desligamento':
        self.abortShutdown()

  def checkAmountOfTime(self, timeToCheck):

    if self.values['timeInMinutes'] == True:
      self.getTimeInputinSeconds(timeToCheck)
      self.showLog(timeToCheck)
    
    if self.values['timeInHours'] == True:
      self.setTimeInHours(timeToCheck)
      self.showLog(timeToCheck)

  def setTimeInHours(self, getTimeToConvert):
    hourToMinute = getTimeToConvert * 60
    minuteInSeconds = hourToMinute * 60
    print(f'shutdown /s /t {minuteInSeconds}')
    return os.system(f'shutdown /s /t {minuteInSeconds}')
    
  def getTimeInputinSeconds(self, timeInMinutes):
    timeInSeconds = timeInMinutes * 60
    print(f'shutdown /s /t {timeInSeconds}')
    return os.system(f'shutdown /s /t {timeInSeconds}')
    

  def abortShutdown(self):
    self.mainWindow['Log'+sg.WRITE_ONLY_KEY].print(f'Desligamento cancelado!', text_color='red')
    return os.system("shutdown /a")

  def showLog(self, inputtedTime):

    if self.values['timeInMinutes'] == True:
      self.mainWindow['Log'+sg.WRITE_ONLY_KEY].print(f'O computador irá se desligar em {inputtedTime} minutos')
    
    if self.values['timeInHours'] == True:
      return self.mainWindow['Log'+sg.WRITE_ONLY_KEY].print(f'O computador irá se desligar em {inputtedTime} horas')

shutdown = ScheduledShutdown()
shutdown.startApp()