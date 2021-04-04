from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectRelationship(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Relationship']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleRelationship(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalRelationship = 'Relationship:'
    for relationship in options['Relationship']:
        originalRelationship += relationship + ','
    if originalRelationship[-1] == ',': originalRelationship = originalRelationship[:-1]
    if listbox.get(index) not in options['Relationship']:
        options['Relationship'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Relationship'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newRelationship = 'Relationship:'
    for relationship in options['Relationship']:
        newRelationship += relationship + ','
    if newRelationship[-1] == ',': newRelationship = newRelationship[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalRelationship), str(newRelationship)))

def relationshipEdit(tab_parent, options):
    # Relationship Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Relationship")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    relationshipListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 14), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    relationships = ['Monogamous', 'Non-monogamous', 'Open to either']
    for index, relationship in enumerate(relationships):
        relationshipListbox.insert(tk.END, relationship)
        if relationship in options['Relationship']:
            relationshipListbox.itemconfig(index, bg=invalid_color)
    relationshipListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=relationshipListbox, options=options: toggleRelationship(relationshipListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    relationshipListbox.bind('<<ListboxSelect>>', lambda event, listbox=relationshipListbox: selectRelationship(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a relationship type will swipe left\non all profiles seeking that relationship type", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))