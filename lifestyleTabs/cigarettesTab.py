from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectCigarettes(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Cigarettes']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleCigarettes(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalCigarettes = 'Cigarettes:'
    for cigarettes in options['Cigarettes']:
        originalCigarettes += cigarettes + ','
    if originalCigarettes[-1] == ',': originalCigarettes = originalCigarettes[:-1]
    if listbox.get(index) not in options['Cigarettes']:
        options['Cigarettes'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Cigarettes'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newCigarettes = 'Cigarettes:'
    for cigarettes in options['Cigarettes']:
        newCigarettes += cigarettes + ','
    if newCigarettes[-1] == ',': newCigarettes = newCigarettes[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalCigarettes), str(newCigarettes)))

def cigarettesEdit(tab_parent, options):
    # Cigarettes Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Cigarettes")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    cigarettesListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 14), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    cigarettes = ['Smokes cigarettes regularly', 'Smokes cigarettes sometimes', "Doesn't smoke cigarettes"]
    for index, cigarettes in enumerate(cigarettes):
        cigarettesListbox.insert(tk.END, cigarettes)
        if cigarettes in options['Cigarettes']:
            cigarettesListbox.itemconfig(index, bg=invalid_color)
    cigarettesListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=cigarettesListbox, options=options: toggleCigarettes(cigarettesListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    cigarettesListbox.bind('<<ListboxSelect>>', lambda event, listbox=cigarettesListbox: selectCigarettes(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a selection will swipe left\non all profiles with that selection", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))