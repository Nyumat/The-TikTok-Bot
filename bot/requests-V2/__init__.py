
# Imports all the modules for the script.
from os.path import dirname, basename, isfile, join
import glob
import os 

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

# Calls program files
if __name__ == '__init__':
  os.system('python3 __init__.py')
  os.system('python3 main.py')
