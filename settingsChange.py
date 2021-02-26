from resourcePath import resourcePath

def swipesEntrybox(swipes):
    term = "Number of Swipes"
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    # convert to term
    nonZeroWrite(term, swipes, CONFIG_FILE)

def percentageEntrybox(percentage):
    term = "Minimum Percentage"
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    # convert to term
    zeroWrite(term, percentage, CONFIG_FILE)

def imagesEntrybox(images):
    term = "Minimum Number of Images"
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    # convert to term
    nonZeroWrite(term, images, CONFIG_FILE)

def wordsEntrybox(words):
    term = "Minimum Word Count"
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    # convert to term
    zeroWrite(term, words, CONFIG_FILE)

def questionsEntrybox(questions):
    term = "Minimum Questions Answered"
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    # convert to term
    zeroWrite(term, questions, CONFIG_FILE)

def nonZeroWrite(term, value, CONFIG_FILE):
    if value.get() == '':
        with open(resourcePath('Settings.txt'), 'wt') as file:
                file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(1)))
    else:
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(value.get())))
    file.close()

def zeroWrite(term, value, CONFIG_FILE):
    if value.get() == '':
        with open(resourcePath('Settings.txt'), 'wt') as file:
                file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(0)))
    else:
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index('\n', CONFIG_FILE.index(term) + len(term))]), str(str(CONFIG_FILE[CONFIG_FILE.index(term) + 1:CONFIG_FILE.index(':', CONFIG_FILE.index(term)) + 1])) + str(value.get())))
    file.close()

# check if input is an integer, reject if not
def checkInt(value, newTotal, type):
    try:
        int(value)
        if type == "swipes":
            if newTotal == '' or int(newTotal) <= 300 and not ('0' in newTotal and len(newTotal) >= 1 and newTotal[0] == '0'): return True
        elif type == "compatibility":
            if newTotal == '' or int(newTotal) <= 100 and not ('0' in newTotal and len(newTotal) >= 2 and newTotal[0] == '0'): return True
        elif type == "images":
            if newTotal == '' or int(newTotal) <= 9 and int(newTotal) != 0: return True
        elif type == "words":
            if newTotal == '' or int(newTotal) <= 300 and not ('0' in newTotal and len(newTotal) >= 2 and newTotal[0] == '0'):return True
        elif type == "questions":
            if newTotal == '' or int(newTotal) <= 1000 and not ('0' in newTotal and len(newTotal) >= 2 and newTotal[0] == '0'): return True
        return False
    except ValueError:
        return False
