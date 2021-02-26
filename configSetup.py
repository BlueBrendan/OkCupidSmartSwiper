import tkinter as tk
from resourcePath import resourcePath
import os

def readConfigFile():
    CONFIG_FILE = open(resourcePath("Settings.txt"), 'r').read()
    options = {}
    terms = ['Number of Swipes', 'Minimum Percentage', 'Minimum Number of Images', 'Minimum Word Count', 'Minimum Questions Answered']
    for term in terms:
        try:
            value = int(CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1: CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))])
            options[term] = tk.IntVar(value=value)
        except:
            os.remove(resourcePath('Settings.txt'))
            createConfigFile()
            readConfigFile()
    return options

def createConfigFile():
    # create settings file
    file = open("Settings.txt", 'w')
    file.write("Number of Swipes:100\nMinimum Percentage:95\nMinimum Number of Images:3\nMinimum Word Count:100\nMinimum Questions Answered:100\n")
    file.close()