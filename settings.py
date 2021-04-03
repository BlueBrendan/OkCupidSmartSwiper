import tkinter as tk
import os
import sys

def resourcePath(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def readConfigFile(bg, secondary_bg):
    CONFIG_FILE = open(resourcePath("Settings.txt"), 'r').read()
    options = {}
    terms = ['Number of Swipes', 'Check Percentage', 'Minimum Percentage', 'Check Images',  'Minimum Number of Images', 'Check Words',  'Minimum Word Count', 'Check Questions',  'Minimum Questions Answered', 'Orientation', 'Body Type', 'Ethnicity', 'Education', 'Religion', 'Phrases', 'Check Criteria', 'Check Intro']
    for term in terms:
        if term[0:5] == 'Check':
            try:
                value = CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1: CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]
                options[term] = tk.BooleanVar(value=value)
            except:
                os.remove(resourcePath('Settings.txt'))
                createConfigFile(bg, secondary_bg)
                readConfigFile(bg, secondary_bg)
        elif term[0:12] == 'Orientation' or term[0:4] == 'Body' or term[0:11] == 'Ethnicity' or term[0:7] == 'Phrases' or term[0:8] == 'Religion' or term[0:9] == 'Education':
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
    file.write("Number of Swipes:100\nCheck Percentage:True\nMinimum Percentage:95\nCheck Images:True\nMinimum Number of Images:3\nCheck Words:True\nMinimum Word Count:100\nCheck Questions:True\nMinimum Questions Answered:100\nOrientation:\nBody Type:\nEthnicity:\nEducation:\nReligion:\nPhrases:fluent in sarcasm,can't see likes,cant see likes,handle me at my worst,i'm a nice guy,im a nice guy\nCheck Criteria:True\nCheck Intro:True\n")
    file.close()

def zeroEntrybox(item, term):
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    # convert to term
    if item.get() == '':
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(0)))
    else:
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(item.get())))
    file.close()

def nonZeroEntrybox(item, term):
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    # convert to term
    if item.get() == '':
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(1)))
    else:
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(item.get())))
    file.close()

def checkbuttonClick(entrybox, term):
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    if CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))] == "True":
        if type(entrybox) != bool: entrybox.config(state=tk.DISABLED)
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1]) + "True", str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + "False"))
        file.close()
    elif CONFIG_FILE[CONFIG_FILE.index(term) + len(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))] == "False":
        if type(entrybox) != bool: entrybox.config(state=tk.NORMAL)
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1]) + "False", str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + "True"))
        file.close()

# check if input is an integer, reject if not
def checkInt(value, newTotal, type):
    try:
        int(value)
        if type == "swipes":
            if newTotal == '' or int(newTotal) <= 1000 and len(str(newTotal)) <= 4: return True
        elif type == "compatibility":
            if newTotal == '' or int(newTotal) <= 100  and len(str(newTotal)) <= 3: return True
        elif type == "images":
            if newTotal == '' or int(newTotal) <= 9 and int(newTotal) != 0: return True
        elif type == "words":
            if newTotal == '' or int(newTotal) <= 300 and len(str(newTotal)) <= 3:return True
        elif type == "questions":
            if newTotal == '' or int(newTotal) <= 1000 and len(str(newTotal)) <= 4: return True
        return False
    except ValueError:
        return False
