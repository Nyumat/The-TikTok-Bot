import os
import time
from os import system

def installLibraries():
    
   print(f'Installing Libraries....')
   time.sleep(45)
  
   system('pip install requests')
   system('pip install threading')
   system('pip install bs4')
   system('pip install time')
   system('pip install math')
   system('pip install selenium')
   system('pip install Keys')
   system('pip install ActionsChains')
   system('pip install sys')
   system('pip install multiprocessing')
   system('pip install logging')
          
installLibraries()
          
print(f'\n'+'All Required Libraries are now installed.')
os.exit()
