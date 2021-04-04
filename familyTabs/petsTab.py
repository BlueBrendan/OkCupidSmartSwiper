from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectPets(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Pets']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def togglePets(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalPets = 'Pets:'
    for pets in options['Pets']:
        originalPets += pets + ','
    if originalPets[-1] == ',': originalPets = originalPets[:-1]
    if listbox.get(index) not in options['Pets']:
        options['Pets'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Pets'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newPets = 'Pets:'
    for pets in options['Pets']:
        newPets += pets + ','
    if newPets[-1] == ',': newPets = newPets[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalPets), str(newPets)))

def petsEdit(tab_parent, options):
    # Pets Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Pets")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    petsListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 14), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    pets = ["Doesn't have pet(s)", "Has other pet(s)",  "Has cat(s)", "Has dog(s)"]
    for index, pets in enumerate(pets):
        petsListbox.insert(tk.END, pets)
        if pets in options['Pets']:
            petsListbox.itemconfig(index, bg=invalid_color)
    petsListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=petsListbox, options=options: togglePets(petsListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    petsListbox.bind('<<ListboxSelect>>', lambda event, listbox=petsListbox: selectPets(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a selection will swipe left\non all profiles with that selection", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))