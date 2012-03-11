import os
import pat
import string
import sys

#this makes sure the program will work in any directory
def get_path():
    PAT = str(pat).split()[3][1:-9]
    sig = None
    try:
        sig = os.remove(PAT + 'pay.pyc')
    except OSError:
        PAT = os.path.join(PAT, '')
    return PAT
path = get_path()


