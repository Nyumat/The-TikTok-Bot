<p align="center">
  <img width="460" height="300" src="https://tricolortimes.com/wp-content/uploads/2020/02/Reviews_Larsen-Whitnie_TikTok.svg">
  
  -----![](https://img.shields.io/badge/updated-today-brightgreen)![](https://img.shields.io/badge/license-MIT-green)![](https://img.shields.io/badge/python%40master-v3.7-blue)![](https://img.shields.io/badge/version-v2-blue)![](https://img.shields.io/badge/docs-94%25-green)![](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)![](https://img.shields.io/badge/requirements-up%20to%20date-brightgreen)----

#       --------------->     The TikTik Bot (Work-In Progress!)      <--------------

<b><p align="center">Disclaimer: This bot is for educational purposes, only.</p></b>

# How to run the program(s)

* Install file from .zip
* Make Sure pip is added to PATH
* Run setup.py if you don't have the required modules
* Run `autoViews.py` or equivalent

If you don't already know how to make a Python virtual enviornment, please keep reading.
```
mkdir my-new-python-project
cd my-new-python-project
virtualenv --python=python(your-python-version) venv # *No parenthesis*
# This will create a my-new-python-project/venv folder
touch .gitignore
subl .gitignore
# Add venv to your .gitignore
```
Whenever you'd like to re-run the program, you have to activate the enviornment:
```
lsvirtualenv - List all of your enviornments.
cd my-new-python-project
source venv/bin/activate
```
Once it's activated, if you haven't already run setup.py, you can install the libraries.
```
pip install requests
pip install threading
pip install selenium
pip install etc. etc.
```
*Once you do this you'll finally be good to go!*

# To-Do:

- [ ] Implement the multiprocessing module for the ability to trigger two ports at once
- [x] Complete Documentation
- [ ] Add captcha bypass in selenium version
- [ ] Create a system for scraping proxies from the [freeproxylist.net](freeproxylist.net) website
- [ ] Incooperate another bot object, that runs inline with the main bot.
- [x] Finish refactoring the old share bot. 

# License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
