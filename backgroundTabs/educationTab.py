from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectEducation(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Education']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleEducation(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalEducation = 'Education:'
    for education in options['Education']:
        originalEducation += education + ','
    if originalEducation[-1] == ',': originalEducation = originalEducation[:-1]
    if listbox.get(index) not in options['Education']:
        options['Education'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Education'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newEducation = 'Education:'
    for education in options['Education']:
        newEducation += education + ','
    if newEducation[-1] == ',': newEducation = newEducation[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalEducation), str(newEducation)))

def educationEdit(tab_parent, options):
    # Education Tab
    tab3 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab3, text="Education")

    listboxContainer = tk.Frame(tab3, bg=bg)
    listboxContainer.pack()
    educationListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    educations = ['High school', 'Trade/tech school', 'In college', 'Undergraduate degree']
    for index, education in enumerate(educations):
        educationListbox.insert(tk.END, education)
        if education in options['Education']:
            educationListbox.itemconfig(index, bg=invalid_color)
    educationListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=educationListbox, options=options: toggleEducation(educationListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    educationListbox.bind('<<ListboxSelect>>', lambda event, listbox=educationListbox: selectEducation(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab3, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling an education will swipe left\non all profiles identifying as having that education", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))