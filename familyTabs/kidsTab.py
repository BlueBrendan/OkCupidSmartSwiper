from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectKids(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Kids']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleKids(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalKids = 'Kids:'
    for kids in options['Kids']:
        originalKids += kids + ','
    if originalKids[-1] == ',': originalKids = originalKids[:-1]
    if listbox.get(index) not in options['Kids']:
        options['Kids'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Kids'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newKids = 'Kids:'
    for kids in options['Kids']:
        newKids += kids + ','
    if newKids[-1] == ',': newKids = newKids[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalKids), str(newKids)))

def kidsEdit(tab_parent, options):
    # Kids Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Kids")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    kidsListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 14), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    kids = ['Has kid(s)', "Doesn't have kids"]
    for index, kids in enumerate(kids):
        kidsListbox.insert(tk.END, kids)
        if kids in options['Kids']:
            kidsListbox.itemconfig(index, bg=invalid_color)
    kidsListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=kidsListbox, options=options: toggleKids(kidsListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    kidsListbox.bind('<<ListboxSelect>>', lambda event, listbox=kidsListbox: selectKids(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a selection will swipe left\non all profiles with that selection", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))