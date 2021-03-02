import tkinter as tk
from resourcePath import resourcePath
import os

def readConfigFile(bg, secondary_bg):
    CONFIG_FILE = open(resourcePath("Settings.txt"), 'r').read()
    options = {}
    terms = ['Number of Swipes', 'Check Percentage', 'Minimum Percentage', 'Check Images',  'Minimum Number of Images', 'Check Words',  'Minimum Word Count', 'Check Questions',  'Minimum Questions Answered', 'Body Types', 'Ethnicities', 'Phrases']
    for term in terms:
        if term[0:5] == 'Check':
            try:
                value = CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1: CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]
                options[term] = tk.BooleanVar(value=value)
            except:
                os.remove(resourcePath('Settings.txt'))
                createConfigFile(bg, secondary_bg)
                readConfigFile(bg, secondary_bg)
        elif term[0:4] == 'Body' or term[0:11] == 'Ethnicities' or term[0:7] == 'Phrases':
            try:
                values = CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1: CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]
                if values == '':
                    options[term] = []
                else:
                    options[term] = values.split(',')
            except:
                os.remove(resourcePath('Settings.txt'))
                createConfigFile(bg, secondary_bg)
                readConfigFile(bg, secondary_bg)
        else:
            try:
                value = int(CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1: CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))])
                options[term] = tk.IntVar(value=value)
            except:
                os.remove(resourcePath('Settings.txt'))
                createConfigFile(bg, secondary_bg)
                readConfigFile(bg, secondary_bg)
    return options


def createConfigFile(bg, secondary_bg):
    # create settings file
    file = open("Settings.txt", 'w')
    file.write("Number of Swipes:500\nCheck Percentage:True\nMinimum Percentage:95\nCheck Images:True\nMinimum Number of Images:3\nCheck Words:True\nMinimum Word Count:120\nCheck Questions:True\nMinimum Questions Answered:150\nBody Types:\nEthnicities:\nPhrases:fluent in sarcasm,can't see likes,cant see likes,handle me at my worst\n")
    file.close()