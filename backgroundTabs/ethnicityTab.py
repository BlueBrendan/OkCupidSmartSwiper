from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectEthnicity(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Ethnicity']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleEthnicity(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalEthnicities = 'Ethnicity:'
    for ethnicity in options['Ethnicity']:
        originalEthnicities += ethnicity + ','
    if originalEthnicities[-1] == ',': originalEthnicities = originalEthnicities[:-1]
    if listbox.get(index) not in options['Ethnicity']:
        options['Ethnicity'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Ethnicity'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newEthnicities = 'Ethnicity:'
    for ethnicity in options['Ethnicity']:
        newEthnicities += ethnicity + ','
    if newEthnicities[-1] == ',': newEthnicities = newEthnicities[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalEthnicities), str(newEthnicities)))

def ethnicityEdit(tab_parent, options):
    # Ethnicity Tab
    tab2 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab2, text="Ethnicity")

    listboxContainer = tk.Frame(tab2, bg=bg)
    listboxContainer.pack()
    ethnicityListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    ethnicities = ['Asian', 'Black', 'Hispanic/Latin', 'Indian', 'Middle Eastern', 'Native American', 'Pacific Islander', 'White', 'Other']
    for index, ethnicity in enumerate(ethnicities):
        ethnicityListbox.insert(tk.END, ethnicity)
        if ethnicity in options['Ethnicity']:
            ethnicityListbox.itemconfig(index, bg=invalid_color)
    ethnicityListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=ethnicityListbox, options=options: toggleEthnicity(ethnicityListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    ethnicityListbox.bind('<<ListboxSelect>>', lambda event, listbox=ethnicityListbox: selectEthnicity(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab2, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling an ethnicity will swipe left\non all profiles identifying as that ethnicity", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))