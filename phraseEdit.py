from settings import resourcePath
import tkinter as tk
from sys import platform

invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectPhrase(button):
    try:
        button.config(state=tk.NORMAL)
    except:
        pass

def phraseRemove(listbox, removeButton, options):
    index = int(listbox.curselection()[0])
    # remove phrase from settings file
    originalPhrases = 'Phrases:'
    for phrase in options['Phrases']:
        originalPhrases += phrase + ','
    if originalPhrases[-1] == ',': originalPhrases = originalPhrases[:-1]
    options['Phrases'].remove(listbox.get(index))
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newPhrases = 'Phrases:'
    for phrase in options['Phrases']:
        newPhrases += phrase + ','
    if newPhrases[-1] == ',': newPhrases = newPhrases[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalPhrases), str(newPhrases)))
    listbox.delete(index)
    removeButton.config(state=tk.DISABLED)

def phraseAddPrompt(phraseListbox, options, bg, secondary_bg):
    addPhraseWindow = tk.Toplevel()
    addPhraseWindow.title("Add Phrase")
    ws = addPhraseWindow.winfo_screenwidth()  # width of the screen
    hs = addPhraseWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (180 / 2)
    addPhraseWindow.geometry('%dx%d+%d+%d' % (500, 180, x, y))
    addPhraseWindow.configure(bg=bg)
    if platform == 'win32':
        addPhraseWindow.iconbitmap(resourcePath('favicon.ico'))
    mainContainer = tk.Frame(addPhraseWindow, bg=bg)
    mainContainer.pack()
    newPhrase = tk.StringVar()
    tk.Label(mainContainer, text="Enter a new phrase", font=('Symphonie Grotesque', 15), fg="white", bg=bg).pack(pady=(20, 0))
    tk.Entry(mainContainer, textvariable=newPhrase, width=40, font=("Symphonie Grotesque", 14), highlightbackground="black").pack(pady=(15, 0))
    tk.Button(mainContainer, text="ADD", command=lambda: phraseAdd(phraseListbox, options, newPhrase, addPhraseWindow, bg, secondary_bg), width=5, font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(25,0))

def phraseAdd(phraseListbox, options, newPhrase, addPhraseWindow, bg, secondary_bg):
    duplicate = False
    for phrase in options['Phrases']:
        if phrase.lower() in newPhrase.get().lower():
            duplicate = True
            break
    if duplicate:
        phraseWarningWindow = tk.Toplevel()
        phraseWarningWindow.title("Error Adding Phrase")
        ws = phraseWarningWindow.winfo_screenwidth()  # width of the screen
        hs = phraseWarningWindow.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (350 / 2)
        y = (hs / 2) - (180 / 2)
        phraseWarningWindow.geometry('%dx%d+%d+%d' % (350, 180, x, y))
        phraseWarningWindow.configure(bg=bg)
        tk.Label(phraseWarningWindow, text="This phrase (or a subset of the phrase) is already saved in the list. Phrases must be unique", wraplength=270, font=('Symphonie Grotesque', 14), fg="white", bg=bg).pack(pady=(20, 0))
        tk.Button(phraseWarningWindow, text="OK", command=lambda: phraseWarningWindow.destroy(), width=5, font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(25, 0))
    else:
        # write phrase to settings file
        originalPhrases = 'Phrases:'
        for phrase in options['Phrases']:
            originalPhrases += phrase + ','
        if originalPhrases[-1] == ',': originalPhrases = originalPhrases[:-1]
        options['Phrases'].append(newPhrase.get())
        # write to settings file
        CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
        newPhrases = 'Phrases:'
        for phrase in options['Phrases']:
            newPhrases += phrase + ','
        if newPhrases[-1] == ',': newPhrases = newPhrases[:-1]
        with open(resourcePath('Settings.txt'), 'wt') as file:
            file.write(CONFIG_FILE.replace(str(originalPhrases), str(newPhrases)))
        phraseListbox.insert(tk.END, newPhrase.get())
        addPhraseWindow.destroy()

def onClose(button, window):
    button.config(state=tk.NORMAL)
    window.destroy()

def phraseEdit(options, button, bg, secondary_bg, tertiary_bg):
    # disable body type button until window is closed
    button.config(state=tk.DISABLED)
    quaternary_bg = "#2f3346"
    phraseWindow = tk.Toplevel()
    phraseWindow.title("Phrase Preferences")
    ws = phraseWindow.winfo_screenwidth()  # width of the screen
    hs = phraseWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (400 / 2)
    phraseWindow.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    phraseWindow.configure(bg=bg)

    listboxContainer = tk.Frame(phraseWindow, bg=bg)
    listboxContainer.pack()
    phraseListbox = tk.Listbox(listboxContainer,  font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg,  highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')

    for index, phrase in enumerate(options['Phrases']):
        phraseListbox.insert(tk.END, phrase)
    phraseListbox.pack(pady=(35, 0))
    phraseListbox.bind('<<ListboxSelect>>', lambda event, listbox=phraseListbox: selectPhrase(removeButton))

    buttonContainer = tk.Frame(phraseWindow, bg=bg)
    buttonContainer.pack(pady=(20, 0))
    tk.Button(buttonContainer, text="ADD", command=lambda: phraseAddPrompt(phraseListbox, options, bg, secondary_bg), width=7, font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(side="left", padx=(0, 15))
    removeButton = tk.Button(buttonContainer, text="REMOVE", command=lambda: phraseRemove(phraseListbox, removeButton, options), width=8, state=tk.DISABLED, font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white")
    removeButton.pack(side="right", padx=(15, 0))

    description = tk.Frame(phraseWindow, bg=bg)
    description.pack()
    tk.Label(description, text="The program will swipe left on all profiles that use any of the phrases above in their bio. Phrases are NOT case sensitive", wraplength=450, font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(20, 0))

    phraseWindow.protocol("WM_DELETE_WINDOW", lambda button=button, window=phraseWindow: onClose(button, window))