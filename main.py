from login import login
from settingsChange import swipesEntrybox, percentageEntrybox, imagesEntrybox, wordsEntrybox, questionsEntrybox, checkInt
from configSetup import readConfigFile, createConfigFile
from resourcePath import resourcePath
import tkinter as tk
import os

# main driver code
bg = "#282f3b"
secondary_bg = "#ff4ec0"
root = tk.Tk()
root.title("OkCupid Smart Swipe")
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (1200/2)
y = (hs/2) - (400/2)
root.geometry('%dx%d+%d+%d' % (1200, 400, x, y))
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
swipesContainerTitle = tk.Label(swipesContainer, text="Number of\nSwipes to Perform (1-300)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
swipes = tk.StringVar(value=options['Number of Swipes'].get())
swipes.trace("w", lambda name, index, mode, swipes=swipes: swipesEntrybox(swipes))
swipesEntry = tk.Entry(swipesContainer, width=5, textvariable=swipes, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
# validate input
validate = (swipesEntry.register(checkInt))
swipesEntry.configure(validatecommand=(validate, '%S', '%P', "swipes"))
swipesEntry.pack(anchor="w", padx=(3, 0))

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

# number of images threshold selection
imagesContainer = tk.Frame(optionsTopRow, bg=bg)
imagesContainer.pack(side="left", padx=(50, 0))
imagesContainerTitle = tk.Label(imagesContainer, text="Minimum Number\nof Images (1-9)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
images = tk.StringVar(value=options['Minimum Number of Images'].get())
images.trace("w", lambda name, index, mode, images=images: imagesEntrybox(images))
imagesContainerEntry = tk.Entry(imagesContainer, width=5, textvariable=images, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
# validate input
validate = (imagesContainerEntry.register(checkInt))
imagesContainerEntry.configure(validatecommand=(validate, '%S', '%P', "images"))
imagesContainerEntry.pack(anchor="w", padx=(3, 0))

# number of words threshold selection
wordsContainer = tk.Frame(optionsTopRow, bg=bg)
wordsContainer.pack(side="left", padx=(50, 0))
wordsContainerTitle = tk.Label(wordsContainer, text="Minimum Word\nCount in Bio (0-300)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
words = tk.StringVar(value=options['Minimum Word Count'].get())
words.trace("w", lambda name, index, mode, words=words: wordsEntrybox(words))
wordsContainerEntry = tk.Entry(wordsContainer, width=5, textvariable=words, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
# validate input
validate = (wordsContainerEntry.register(checkInt))
wordsContainerEntry.configure(validatecommand=(validate, '%S', '%P', "words"))
wordsContainerEntry.pack(anchor="w", padx=(3, 0))

# number of questions threshold selection
questionsContainer = tk.Frame(optionsTopRow, bg=bg)
questionsContainer.pack(side="left", padx=(50, 0))
questionsContainerTitle = tk.Label(questionsContainer, text="Minimum Number\nof Questions Answered (0-1000)", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
questions = tk.StringVar(value=options['Minimum Questions Answered'].get())
questions.trace("w", lambda name, index, mode, questions=questions: questionsEntrybox(questions))
questionsContainerEntry = tk.Entry(questionsContainer, width=5, textvariable=questions, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black")
# validate input
validate = (questionsContainerEntry .register(checkInt))
questionsContainerEntry .configure(validatecommand=(validate, '%S', '%P', "questions"))
questionsContainerEntry .pack(anchor="w", padx=(3, 0))

startButton = tk.Button(mainContainer, text="BEGIN SWIPING", command=lambda: login(options), font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(50, 0))
bottomText = tk.Label(mainContainer, text="OkCupid Smart Swipe exists solely to enhance the swiping experience and is completely unaffiliated with OkCupid", font=('Symphonie Grotesque', 10), fg="white", bg=bg, highlightthickness=0).pack(pady=(70, 0))
root.mainloop()

