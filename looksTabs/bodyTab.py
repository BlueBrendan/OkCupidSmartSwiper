from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectBodyType(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Body Type']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleBodyType(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalBodyType = 'Body Type:'
    for bodyType in options['Body Type']:
        originalBodyType += bodyType + ','
    if originalBodyType[-1] == ',': originalBodyType = originalBodyType[:-1]
    if listbox.get(index) not in options['Body Type']:
        options['Body Type'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Body Type'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newBodyType = 'Body Type:'
    for bodyType in options['Body Type']:
        newBodyType += bodyType + ','
    if newBodyType[-1] == ',': newBodyType = newBodyType[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalBodyType), str(newBodyType)))

def bodyEdit(tab_parent, options):
    # Body Type Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Body Type")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    bodyTypeListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    bodyTypes = ['Thin', 'Average', 'Fit', 'Jacked', 'A little extra', 'Overweight', 'Curvy', 'Full Figured']
    for index, bodyType in enumerate(bodyTypes):
        bodyTypeListbox.insert(tk.END, bodyType)
        if bodyType in options['Body Type']:
            bodyTypeListbox.itemconfig(index, bg=invalid_color)
    bodyTypeListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=bodyTypeListbox, options=options: toggleBodyType(bodyTypeListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    bodyTypeListbox.bind('<<ListboxSelect>>', lambda event, listbox=bodyTypeListbox: selectBodyType(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a body type will swipe left\non all profiles identifying as that body type", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))