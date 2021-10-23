# stuycs-submit


![](https://img.shields.io/github/v/release/anivanchen/stuycs-submit?style=for-the-badge)
![](https://img.shields.io/github/license/anivanchen/stuycs-submit?color=brightgreen&style=for-the-badge)

A CLI program to submit homework to the StuyCS homework server (bert.stuy.edu) written in Python and built using BeautifulSoup and requests. This should work in MacOS, Windows, and Linux. 

# Installation / Setup

This program requires the libraries **requests** and **BeautifulSoup** to be installed. You should also have **Python** installed. 

## Verify you have Python installed: 
- `$ py --version` or
- `$ python --version`

If not installed, go to python.org/downloads and install the latest version.

## Install prerequisites BeautifulSoup and requests

- `py -m pip install beautifulsoup4 requests` or
- `pip install beautifulsoup4 requests` or
- `python -m pip install beautifulsoup4 requests`

## Download this code

### Option A

- Run: 
`git clone https://github.com/anivanchen/stuycs-submit`

### Option B 

- Run in a CLI: 
`curl https://raw.githubusercontent.com/anivanchen/stuycs-submit/main/stuycs-submit.py --output stuycs-submit.py`

If you do not have Mr. David M. Holmes

- Run this also: 
`curl https://raw.githubusercontent.com/anivanchen/stuycs-submit/main/getIDs.py --output getIDs.py`

### Option C

- Download the repository from https://github.com/anivanchen/stuycs-submit as a zip file. 
- Extract the zip file. 

## Run this code
If you have Mr. David M. Holmes, you're set. At least for this semester. After the fall2021 term, follow the instructions below if I do not update this repository. Just double click `stuycs-submit.py` and follow the instructions there. 

If you do not have Mr. David M. Holmes, or it is no longer the fall2021 semester, your job is slightly harder. 
- Run `getIDs.py` first and follow the instructions there. 
- A file named `IDs.txt` should be created in the same directory. Open it. 
- Something like `p1 'CHEN, IVAN': 'a739sjaie25',...` should fill every line in the file. The first is the period, the second is the names, and the third is a generated ID by the site. The ID is what we are looking for.
- Open `stuycs-submit.py` in some sort of editor, notepad, vscode, nano, vim, etc. 
- Starting at line 6 is something called a nested dictionary. 
- Remove the existing one. 
- Note the format of the preexisting one. 
```
p = {
  'p1': {
    'EXAMPLE, NAME': 'ID',
    'EXAMPLE, NAME': 'ID',
    'EXAMPLE, NAME': 'ID'
  },
  'p3': {
    'EXAMPLE, NAME': 'ID',
    'EXAMPLE, NAME': 'ID',
    'EXAMPLE, NAME': 'ID'
  }
}
```
- Take the nearly completely formatted text from `IDs.txt` and convert it to the format of the dictonary. 
- You're done!!!
- Exit the editor.
- Double click `stuycs-submit.py` and follow the instructions. 

## Security

The process for this script is entirely local, except for interactions with bert.stuy.edu, so there is no way I will know or be able to collect your passwords. This can be verified by examining the code for this program. 

## Disclaimer

This program is **unofficial** and is not the intended way by the CS department for homework submission. **I am not liable for any errors with your homework submission due to the use of this program.** You should **always verify your homework submission** at http://bert.stuy.edu/[teacherName]/[term]/pages.py.

### Cheers mates. Happy homework submitting. 

Report bugs at https://github.com/anivanchen/stuycs-submit/issues.
