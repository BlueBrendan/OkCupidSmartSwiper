from login import login
from settingsChange import swipesEntrybox, checkbuttonClick, percentageEntrybox, imagesEntrybox, wordsEntrybox, questionsEntrybox, checkInt
from configSetup import readConfigFile, createConfigFile
from bodyTypeEdit import bodyTypeEdit
from resourcePath import resourcePath
import tkinter as tk
import os

# main driver code
bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'

root = tk.Tk()
root.title("OkCupid Smart Swipe")
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (1400/2)
y = (hs/2) - (400/2)
root.geometry('%dx%d+%d+%d' % (1400, 400, x, y))
root.configure(bg=bg)

# retrieve user settings
if not os.path.exists(resourcePath('Settings.txt')): createConfigFile()
options = readConfigFile()

mainContainer = tk.Frame(root, bg=bg)
mainContainer.pack()
title = tk.Label(mainContainer, text="OkCupid Smart Swipe", font=('Symphonie Grotesque', 45), fg="white", bg=bg).pack(pady=(30, 0))
optionsTopRow = tk.Frame(mainContainer, bg=bg)
optionsTopRow.pack(pady=(40, 0))

# number of swipes to perform
swipesContainer = tk.Frame(optionsTopRow, bg=bg)
swipesContainer.pack(side="left")
swipesContainerTitle = tk.Label(swipesContainer, text="Number of\nSwipes to Perform (1-1000)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
swipes = tk.StringVar(value=options['Number of Swipes'].get())
swipes.trace("w", lambda name, index, mode, swipes=swipes: swipesEntrybox(swipes))
swipesEntry = tk.Entry(swipesContainer, width=5, textvariable=swipes, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
# validate input
validate = (swipesEntry.register(checkInt))
swipesEntry.configure(validatecommand=(validate, '%S', '%P', "swipes"))
swipesEntry.pack(anchor="w", padx=(3, 0), pady=(0, 22))

# compatibility percentage threshold selection
compatibilityContainer = tk.Frame(optionsTopRow, bg=bg)
compatibilityContainer.pack(side="left", padx=(50, 0))
compatibilityContainerTitle = tk.Label(compatibilityContainer, text="Minimum Compatibility\nPercentage (0-100)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
percentage = tk.StringVar(value=options['Minimum Percentage'].get())
percentage.trace("w", lambda name, index, mode, percentage=percentage: percentageEntrybox(percentage))
compatibilityEntry = tk.Entry(compatibilityContainer, width=5, textvariable=percentage, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
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
images.trace("w", lambda name, index, mode, images=images: imagesEntrybox(images))
imagesEntry = tk.Entry(imagesContainer, width=5, textvariable=images, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
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
words.trace("w", lambda name, index, mode, words=words: wordsEntrybox(words))
wordsEntry = tk.Entry(wordsContainer, width=5, textvariable=words, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
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
questions.trace("w", lambda name, index, mode, questions=questions: questionsEntrybox(questions))
questionsEntry = tk.Entry(questionsContainer, width=5, textvariable=questions, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
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
buttonsContainer.pack(side="left", padx=(50, 0))
bodyTypeButton = tk.Button(buttonsContainer, text="BODY TYPE", command=lambda: bodyTypeEdit(options, bg, secondary_bg, tertiary_bg), font=('Symphonie Grotesque', 15), fg="white", bg=tertiary_bg, highlightthickness=0, activebackground=tertiary_bg, activeforeground="white").pack(pady=(0, 10))
ethnicityButton = tk.Button(buttonsContainer, text="ETHNICITY", command=lambda: ethnicityEdit(bg, secondary_bg, tertiary_bg), font=('Symphonie Grotesque', 15), fg="white", bg=tertiary_bg, highlightthickness=0, activebackground=tertiary_bg, activeforeground="white").pack(pady=(10, 0))

startButton = tk.Button(mainContainer, text="BEGIN SWIPING", command=lambda: login(), font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(35, 0))
bottomText = tk.Label(mainContainer, text="OkCupid Smart Swipe is a third party utility that exists to enhance the swiping experience on OkCupid", font=('Symphonie Grotesque', 10), fg="white", bg=bg, highlightthickness=0).pack(pady=(60, 0))
root.mainloop()

