#!/usr/bin/python3
from subprocess import call
import shutil
import time
import webbrowser

def button_obed():
    shutil.copy('indexBACKUP.html', 'index.html')

    call(["python", "basta.py"])
    call(["python", "pupek.py"])
    call(["python", "makalu.py"])
    call(["python", "gingilla.py"])
    call(["python", "union.py"])
    call(["python", "babeta.py"])
    call(["python", "sediveho.py"])
    call(["python", "mitrovski.py"])
    call(["python", "tanuki.py"])
    call(["python", "drindy.py"])
    call(["python", "coloseum.py"])

    time.sleep(2)
    webbrowser.open("index.html", autoraise=True)
    quit()

