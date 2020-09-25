import os

def installLibraries():
    
        print(f'Installing Libraries....')
        
        os.system('pip install requests')
        os.system('pip install threading')
        os.system('pip install bs4')
        os.system('pip install time')
        os.system('pip install math')
        os.system('pip install selenium')
        os.system('pip install Keys')
        os.system('pip install ActionsChains')
        os.system('pip install sys')
        os.system('pip install multiprocessing')
        os.system('pip install logging')
        os.system('pip install glob')
          
if __name__ == "__main__":
    installLibraries()
    print(f'\n'+'All Required Libraries are now installed.')
