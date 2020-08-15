
## Imports all the modules for the script.
from os.path import dirname, basename, isfile, join
import glob
import os 

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

## Calls program files

def main:
  if __name__ == '__init__':
    os.system('cls && title [The TikTok Bot]')
    main = TikTok()
    main.scrapeProxyList(1 || 2)
    main.start()
main()
