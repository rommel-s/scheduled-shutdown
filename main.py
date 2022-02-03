from logging import shutdown
import os

shutdown = input("desliga?: ")

if shutdown == 'n':
  exit()

else:
  os.system("shutdown /s /t 3600")