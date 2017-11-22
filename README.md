# Bruteforce-Selenium
A simple program to bruteforce a Wi-Fi login page using selenium and python. Used to bruteforce VOLSBB wifi @ VIT.

## Installation & Usage
- **This tool supports only Python 3**

### Windows

Assuming you have Python 3 ([preferably v3.6 or above to stay away from Unicode errors](https://stackoverflow.com/questions/30539882/whats-the-deal-with-python-3-4-unicode-different-languages-and-windows)) already installed and in PATH.

- Download and extract the zip file from master branch.
- Download [Chrome driver]( https://chromedriver.storage.googleapis.com). Put this in the same directory as the unzipped files. 
- [Google Chrome]( https://www.google.com/chrome/browser/desktop/index.html).
- Open `cmd` and type `pip install -U selenium` to install Selenium.

## Instructions

- Open file usernames.txt, add usernames to bruteforce seperated by a new line character.
- You can edit the 'main.py' to change password-list and URL.
- Save and run in cmd using "python main.py"

#### Known Issue
- Geckodriver is throwing exception for some reason, whereas chrome works great with the same code. Start a pull-request if someone can suggest a fix.


## License

```The MIT License```
