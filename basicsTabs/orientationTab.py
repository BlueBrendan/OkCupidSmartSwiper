from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectOrientation(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Orientation']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

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

def orientationEdit(tab_parent, options):
    # Orientation Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Orientation")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    orientationListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    orientations = ['Straight', 'Gay', 'Bisexual', 'Asexual', 'Demisexual', 'Homoflexible', 'Heteroflexible', 'Lesbian', 'Pansexual', 'Queer', 'Questioning', 'Gray-asexual', 'Reciprosexual', 'Akiosexual', 'Aceflux', 'Grayromantic', 'Demiromantic', 'Recipromantic', 'Akioromantic', 'Aroflux']
    for index, orientation in enumerate(orientations):
        orientationListbox.insert(tk.END, orientation)
        if orientation in options['Orientation']:
            orientationListbox.itemconfig(index, bg=invalid_color)
    orientationListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=orientationListbox, options=options: toggleOrientation(orientationListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    orientationListbox.bind('<<ListboxSelect>>', lambda event, listbox=orientationListbox: selectOrientation(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling an orientation will swipe left\non all profiles identifying as that orientation", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))