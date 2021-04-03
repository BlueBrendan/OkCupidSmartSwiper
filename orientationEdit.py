from settings import resourcePath
import tkinter as tk
from sys import platform

invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectOrientation(listbox, options, toggleCheckbutton):
    index = int(listbox.curselection()[0])
    toggleCheckbutton.config(state=tk.NORMAL)
    if listbox.get(index) in options['Orientation']:
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
        toggleCheckbutton.deselect()
    else:
        toggleCheckbutton.select()

def toggleOrientation(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalOrientation = 'Orientation:'
    for orientation in options['Orientation']:
        originalOrientation += orientation + ','
    if originalOrientation[-1] == ',': originalOrientation = originalOrientation[:-1]
    if listbox.get(index) not in options['Orientation']:
        options['Orientation'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Orientation'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newOrientation = 'Orientation:'
    for orientation in options['Orientation']:
        newOrientation += orientation + ','
    if newOrientation[-1] == ',': newOrientation = newOrientation[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalOrientation), str(newOrientation)))

def onClose(button, window):
    button.config(state=tk.NORMAL)
    window.destroy()

def orientationEdit(options, button, bg, secondary_bg, tertiary_bg):
    # disable body type button until window is closed
    button.config(state=tk.DISABLED)
    quaternary_bg = "#2f3346"
    orientationWindow = tk.Toplevel()
    orientationWindow.title("Orientation Preferences")
    ws = orientationWindow.winfo_screenwidth()  # width of the screen
    hs = orientationWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (400 / 2)
    orientationWindow.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    orientationWindow.configure(bg=bg)
    if platform == 'win32':
        orientationWindow.iconbitmap(resourcePath('favicon.ico'))
    listboxContainer = tk.Frame(orientationWindow, bg=bg)
    listboxContainer.pack()
    orientationListbox = tk.Listbox(listboxContainer,  font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg,  highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    orientations = ['Straight', 'Gay', 'Bisexual', 'Asexual', 'Demisexual', 'Homoflexible', 'Heteroflexible', 'Lesbian', 'Pansexual', 'Queer', 'Questioning', 'Gray-asexual', 'Reciprosexual', 'Akiosexual', 'Aceflux', 'Grayromantic', 'Demiromantic', 'Recipromantic', 'Akioromantic', 'Aroflux']
    for index, orientation in enumerate(orientations):
        orientationListbox.insert(tk.END, orientation)
        if orientation in options['Orientation']:
            orientationListbox.itemconfig(index, bg=invalid_color)
    orientationListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=orientationListbox,options=options: toggleOrientation(orientationListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    orientationListbox.bind('<<ListboxSelect>>', lambda event, listbox=orientationListbox: selectOrientation(listbox, options, toggleCheckbutton))

    description = tk.Frame(orientationWindow, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling an orientation will swipe left\non all profiles identifying as that orientation", font=('Symphonie Grotesque', 15), fg="white", bg=bg, justify='left').pack(pady=(15, 0))

    orientationWindow.protocol("WM_DELETE_WINDOW", lambda button=button, window=orientationWindow: onClose(button, window))