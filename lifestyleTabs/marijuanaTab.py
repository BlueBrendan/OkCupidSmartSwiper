from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectMarijuana(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Marijuana']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleMarijuana(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalMarijuana = 'Marijuana:'
    for marijuana in options['Marijuana']:
        originalMarijuana += marijuana + ','
    if originalMarijuana[-1] == ',': originalMarijuana = originalMarijuana[:-1]
    if listbox.get(index) not in options['Marijuana']:
        options['Marijuana'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Marijuana'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newMarijuana = 'Marijuana:'
    for marijuana in options['Marijuana']:
        newMarijuana += marijuana + ','
    if newMarijuana[-1] == ',': newMarijuana = newMarijuana[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalMarijuana), str(newMarijuana)))

def marijuanaEdit(tab_parent, options):
    # Marijuana Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Marijuana")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    marijuanaListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 14), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    marijuana = ['Smokes marijuana regularly', 'Smokes marijuana sometimes', "Doesn't smoke marijuana"]
    for index, marijuana in enumerate(marijuana):
        marijuanaListbox.insert(tk.END, marijuana)
        if marijuana in options['Marijuana']:
            marijuanaListbox.itemconfig(index, bg=invalid_color)
    marijuanaListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=marijuanaListbox, options=options: toggleMarijuana(marijuanaListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    marijuanaListbox.bind('<<ListboxSelect>>', lambda event, listbox=marijuanaListbox: selectMarijuana(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a selection will swipe left\non all profiles with that selection", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))