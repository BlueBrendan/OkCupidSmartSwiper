import tkinter as tk
from resourcePath import resourcePath
import os

def readConfigFile():
    CONFIG_FILE = open(resourcePath("Settings.txt"), 'r').read()
    options = {}
    terms = ['Number of Swipes', 'Check Percentage', 'Minimum Percentage', 'Check Images',  'Minimum Number of Images', 'Check Words',  'Minimum Word Count', 'Check Questions',  'Minimum Questions Answered', 'Body Types', 'Ethnicities']
    for term in terms:
        if (term[0:5] == 'Check'):
            try:
                value = CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1: CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]
                options[term] = tk.BooleanVar(value=value)
            except:
                os.remove(resourcePath('Settings.txt'))
                createConfigFile()
                readConfigFile()
        elif term[0:4] == 'Body' or term[0:11] == 'Ethnicities':
            values = CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1: CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]
            try:
                if values == '':
                    options[term] = []
                else:
                    options[term] = values.split(',')
            except:
                os.remove(resourcePath('Settings.txt'))
                createConfigFile()
                readConfigFile()
        else:
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
    file.write("Number of Swipes:100\nCheck Percentage:True\nMinimum Percentage:90\nCheck Images:True\nMinimum Number of Images:3\nCheck Words:True\nMinimum Word Count:50\nCheck Questions:True\nMinimum Questions Answered:50\nBody Types:\nEthnicities:\n")
    file.close()