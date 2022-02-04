import os
from time import sleep as slp

print('''
  >>> DESLIGAMENTO PROGRAMADO <<<
  
Em quanto tempo o PC deve ser desligado?

Insira o valor em minutos:

''')

timeInput = int(input(">> "))

def continueQuestion():
  abortcount = input('deseja abortar?: ')
  if abortcount == 's' or abortcount == 'S':
    return os.system("shutdown /a")


def getTimeTinputinSeconds(timeToShutdown):

  convertedTime = timeToShutdown * 60

  slp(3)
  print(f'O computador irá se desigar em {convertedTime} segundos')
  os.system(f'shutdown /s /t {convertedTime}')
  
  if convertedTime >= 60:
    slp(5)
    continueQuestion()
    input("Você abortou a operação, pressione ENTER para fechar")

getTimeTinputinSeconds(timeInput)