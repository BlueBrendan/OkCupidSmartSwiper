from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectAlcohol(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Alcohol']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleAlcohol(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalAlcohol = 'Alcohol:'
    for alcohol in options['Alcohol']:
        originalAlcohol += alcohol + ','
    if originalAlcohol[-1] == ',': originalAlcohol = originalAlcohol[:-1]
    if listbox.get(index) not in options['Alcohol']:
        options['Alcohol'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Alcohol'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newAlcohol = 'Alcohol:'
    for alcohol in options['Alcohol']:
        newAlcohol += alcohol + ','
    if newAlcohol[-1] == ',': newAlcohol = newAlcohol[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalAlcohol), str(newAlcohol)))

def alcoholEdit(tab_parent, options):
    # Alcohol Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Alcohol")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    alcoholListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 14), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    alcohol = ['Drinks often', 'Drinks sometimes', "Doesn't drink"]
    for index, alcohol in enumerate(alcohol):
        alcoholListbox.insert(tk.END, alcohol)
        if alcohol in options['Alcohol']:
            alcoholListbox.itemconfig(index, bg=invalid_color)
    alcoholListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=alcoholListbox, options=options: toggleAlcohol(alcoholListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    alcoholListbox.bind('<<ListboxSelect>>', lambda event, listbox=alcoholListbox: selectAlcohol(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a selection will swipe left\non all profiles with that selection", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))