from handleStartup import login
from settings import readConfigFile, createConfigFile, zeroEntrybox, nonZeroEntrybox, checkbuttonClick, checkInt, resourcePath
from orientationEdit import orientationEdit
from bodyTypeEdit import bodyTypeEdit
from ethnicityEdit import ethnicityEdit
from phraseEdit import phraseEdit
from sys import platform
import tkinter as tk
from tkinter import *
import os

if platform == 'win32':
    from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

    # install font if not present
    FR_PRIVATE  = 0x10
    FR_NOT_ENUM = 0x20
    def loadfont(fontpath, private=True, enumerable=False):
        if isinstance(fontpath, bytes):
            pathbuf = create_string_buffer(fontpath)
            AddFontResourceEx = windll.gdi32.AddFontResourceExA
        elif isinstance(fontpath, str):
            pathbuf = create_unicode_buffer(fontpath)
            AddFontResourceEx = windll.gdi32.AddFontResourceExW
        else: raise TypeError('fontpath must be of type str or unicode')
        flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
        numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
        return bool(numFontsAdded)

    loadfont(resourcePath('Symphonie Grotesque.ttf'))

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'

# main driver code
root = tk.Tk()
root.title("OkCupid Smart Swiper")
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (1400/2)
y = (hs/2) - (430/2)
root.geometry('%dx%d+%d+%d' % (1400, 430, x, y))
root.configure(bg=bg)
if platform == 'win32':
    root.Ficonbitmap(resourcePath('favicon.ico'))

# retrieve user settings
if not os.path.exists(resourcePath('Settings.txt')):
    createConfigFile(bg, secondary_bg)
options = readConfigFile(bg, secondary_bg)

mainContainer = tk.Frame(root, bg=bg)
mainContainer.pack()
title = tk.Label(mainContainer, text="OkCupid Smart Swiper", font=('Symphonie Grotesque', 45), fg="white", bg=bg).pack(pady=(40, 0))
optionsTopRow = tk.Frame(mainContainer, bg=bg)
optionsTopRow.pack(pady=(40, 0))

# number of swipes to perform
swipesContainer = tk.Frame(optionsTopRow, bg=bg)
swipesContainer.pack(side="left")
swipesContainerTitle = tk.Label(swipesContainer, text="Number of\nSwipes to Perform (0-1000)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
swipes = tk.StringVar(value=options['Number of Swipes'].get())
swipes.trace("w", lambda name, index, mode, swipes=swipes: zeroEntrybox(swipes, "Number of Swipes"))
swipesEntry = tk.Entry(swipesContainer, width=5, textvariable=swipes, validate="key", font=("Symphonie Grotesque", 14), highlightbackground="black")
# validate input
validate = (swipesEntry.register(checkInt))
swipesEntry.configure(validatecommand=(validate, '%S', '%P', "swipes"))
swipesEntry.pack(anchor="w", padx=(3, 0), pady=(0, 22))

# compatibility percentage threshold selection
compatibilityContainer = tk.Frame(optionsTopRow, bg=bg)
compatibilityContainer.pack(side="left", padx=(50, 0))
compatibilityContainerTitle = tk.Label(compatibilityContainer, text="Minimum Compatibility\nPercentage (0-100)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
percentage = tk.StringVar(value=options['Minimum Percentage'].get())
percentage.trace("w", lambda name, index, mode, percentage=percentage: zeroEntrybox(percentage, 'Minimum Percentage'))
compatibilityEntry = tk.Entry(compatibilityContainer, width=5, textvariable=percentage, validate="key", font=("Symphonie Grotesque", 14), highlightbackground="black")
# validate input
validate = (compatibilityEntry.register(checkInt))
compatibilityEntry.configure(validatecommand=(validate, '%S', '%P', "compatibility"))
compatibilityEntry.pack(anchor="w", padx=(3, 0))
if not options['Check Percentage'].get():
    compatibilityEntry.config(state=tk.DISABLED)
compatibilityCheckbutton = tk.Checkbutton(compatibilityContainer, variable=options['Check Percentage'], bg=bg, highlightbackground=bg, activebackground=bg, command=lambda: checkbuttonClick(compatibilityEntry, "Check Percentage"))
compatibilityCheckbutton.pack(anchor="w", pady=(10, 0))

# number of images threshold selection
imagesContainer = tk.Frame(optionsTopRow, bg=bg)
imagesContainer.pack(side="left", padx=(50, 0))
imagesContainerTitle = tk.Label(imagesContainer, text="Minimum Number\nof Images (1-9)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
images = tk.StringVar(value=options['Minimum Number of Images'].get())
images.trace("w", lambda name, index, mode, images=images: nonZeroEntrybox(images, 'Minimum Number of Images'))
imagesEntry = tk.Entry(imagesContainer, width=5, textvariable=images, validate="key", font=("Symphonie Grotesque", 14), highlightbackground="black")
# validate input
validate = (imagesEntry.register(checkInt))
imagesEntry.configure(validatecommand=(validate, '%S', '%P', "images"))
imagesEntry.pack(anchor="w", padx=(3, 0))
if not options['Check Images'].get():
    imagesEntry.config(state=tk.DISABLED)
imagesCheckbutton = tk.Checkbutton(imagesContainer, variable=options['Check Images'], bg=bg, highlightbackground=bg, activebackground=bg, command=lambda: checkbuttonClick(imagesEntry, "Check Images"))
imagesCheckbutton.pack(anchor="w", pady=(10, 0))

# number of words threshold selection
wordsContainer = tk.Frame(optionsTopRow, bg=bg)
wordsContainer.pack(side="left", padx=(50, 0))
wordsContainerTitle = tk.Label(wordsContainer, text="Minimum Word\nCount in Bio (0-300)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
words = tk.StringVar(value=options['Minimum Word Count'].get())
words.trace("w", lambda name, index, mode, words=words: zeroEntrybox(words, 'Minimum Word Count'))
wordsEntry = tk.Entry(wordsContainer, width=5, textvariable=words, validate="key", font=("Symphonie Grotesque", 14), highlightbackground="black")
# validate input
validate = (wordsEntry.register(checkInt))
wordsEntry.configure(validatecommand=(validate, '%S', '%P', "words"))
wordsEntry.pack(anchor="w", padx=(3, 0))
if not options['Check Words'].get():
    wordsEntry.config(state=tk.DISABLED)
wordsCheckbutton = tk.Checkbutton(wordsContainer, variable=options['Check Words'], bg=bg, highlightbackground=bg, activebackground=bg, command=lambda: checkbuttonClick(wordsEntry, "Check Words"))
wordsCheckbutton.pack(anchor="w", pady=(10, 0))

# number of questions threshold selection
questionsContainer = tk.Frame(optionsTopRow, bg=bg)
questionsContainer.pack(side="left", padx=(50, 0))
questionsContainerTitle = tk.Label(questionsContainer, text="Minimum Number\nof Questions Answered (0-1000)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
questions = tk.StringVar(value=options['Minimum Questions Answered'].get())
questions.trace("w", lambda name, index, mode, questions=questions: zeroEntrybox(questions, 'Minimum Questions Answered'))
questionsEntry = tk.Entry(questionsContainer, width=5, textvariable=questions, validate="key", font=("Symphonie Grotesque", 14), highlightbackground="black")
# validate input
validate = (questionsEntry .register(checkInt))
questionsEntry.configure(validatecommand=(validate, '%S', '%P', "questions"))
questionsEntry.pack(anchor="w", padx=(3, 0))
if not options['Check Questions'].get():
    questionsEntry.config(state=tk.DISABLED)
questionsCheckbutton = tk.Checkbutton(questionsContainer, variable=options['Check Questions'], bg=bg, highlightbackground=bg, activebackground=bg, command=lambda: checkbuttonClick(questionsEntry, "Check Questions"))
questionsCheckbutton.pack(anchor="w", pady=(10, 0))

# number of questions threshold selection
buttonsContainer = tk.Frame(optionsTopRow, bg=bg)
buttonsContainer.pack(padx=(50, 0))
orientationButton = tk.Button(buttonsContainer, text="ORIENTATION", command=lambda: orientationEdit(options, orientationButton, bg, secondary_bg, tertiary_bg), width=11, font=('Symphonie Grotesque', 15), fg="white", bg=tertiary_bg, highlightthickness=0, activebackground=tertiary_bg, activeforeground="white")
orientationButton.pack(pady=(0, 15))
bodyTypeButton = tk.Button(buttonsContainer, text="BODY TYPE", command=lambda: bodyTypeEdit(options, bodyTypeButton, bg, secondary_bg, tertiary_bg), width=11, font=('Symphonie Grotesque', 15), fg="white", bg=tertiary_bg, highlightthickness=0, activebackground=tertiary_bg, activeforeground="white")
bodyTypeButton.pack(pady=(0, 15))
ethnicityButton = tk.Button(buttonsContainer, text="ETHNICITY", command=lambda: ethnicityEdit(options, ethnicityButton, bg, secondary_bg, tertiary_bg), width=11, font=('Symphonie Grotesque', 15), fg="white", bg=tertiary_bg, highlightthickness=0, activebackground=tertiary_bg, activeforeground="white")
ethnicityButton.pack(pady=(0, 15))
phrasesButton = tk.Button(buttonsContainer, text="PHRASES", command=lambda: phraseEdit(options, phrasesButton, bg, secondary_bg, tertiary_bg), width=11, font=('Symphonie Grotesque', 15), fg="white", bg=tertiary_bg, highlightthickness=0, activebackground=tertiary_bg, activeforeground="white")
phrasesButton.pack()




bottomContainer = tk.Frame(mainContainer, bg=bg)
bottomContainer.pack(fill='x', pady=(25, 0))

swipeContainer = tk.Frame(bottomContainer, bg=bg)
swipeContainer.pack(side="left")
swipeCheck = tk.Checkbutton(swipeContainer, variable=options['Check Intro'], bg=bg, highlightbackground=bg, activebackground=bg, command=lambda: checkbuttonClick(False, "Check Intro"))
swipeCheck.pack(side="left")
swipeLabel =tk.Label(swipeContainer, text="Swipe Right Upon Meeting All Criteria", wraplength=150, font=('Symphonie Grotesque', 12), fg='white', bg=bg)
swipeLabel.pack(side="right")

introContainer = tk.Frame(bottomContainer, bg=bg)
introContainer.pack(side="left", padx=(50, 0))
introCheck = tk.Checkbutton(introContainer, variable=options['Check Intro'], bg=bg, highlightbackground=bg, activebackground=bg, command=lambda: checkbuttonClick(False, "Check Intro"))
introCheck.pack(side="left")
introLabel =tk.Label(introContainer, text="Swipe Right on Detecting Intro", wraplength=120, font=('Symphonie Grotesque', 12), fg='white', bg=bg)
introLabel.pack(side="left")

startButton = tk.Button(bottomContainer, text="BEGIN SWIPING", command=lambda: login(root, [startButton, orientationButton, bodyTypeButton, ethnicityButton, phrasesButton], bg, secondary_bg), font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white")
startButton.pack(side="left", padx=(230, 0))

root.mainloop()

