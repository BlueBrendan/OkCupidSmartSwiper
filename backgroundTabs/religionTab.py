from settings import resourcePath
import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = '#47477f'
quaternary_bg = "#2f3346"
invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectReligion(listbox, options, toggleCheckbutton):
    try:
        index = int(listbox.curselection()[0])
        toggleCheckbutton.config(state=tk.NORMAL)
        if listbox.get(index) in options['Religion']:
            listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
            toggleCheckbutton.deselect()
        else:
            toggleCheckbutton.select()
    except IndexError:
        pass

def toggleReligion(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalReligion = 'Religion:'
    for religion in options['Religion']:
        originalReligion += religion + ','
    if originalReligion[-1] == ',': originalReligion = originalReligion[:-1]
    if listbox.get(index) not in options['Religion']:
        options['Religion'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Religion'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newReligion = 'Religion:'
    for religion in options['Religion']:
        newReligion += religion + ','
    if newReligion[-1] == ',': newReligion = newReligion[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalReligion), str(newReligion)))

def religionEdit(tab_parent, options):
    # Religion Tab
    tab1 = tk.Frame(tab_parent, bg=bg)
    tab_parent.add(tab1, text="Religion")

    listboxContainer = tk.Frame(tab1, bg=bg)
    listboxContainer.pack()
    religionListbox = tk.Listbox(listboxContainer, font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg, highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    religions = ['Agnosticism', 'Atheism', 'Christianity', 'Judaism', 'Catholicism', 'Islam', 'Hinduism', 'Buddhism', 'Sikh', 'Other religion']
    for index, religion in enumerate(religions):
        religionListbox.insert(tk.END, religion)
        if religion in options['Religion']:
            religionListbox.itemconfig(index, bg=invalid_color)
    religionListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=religionListbox, options=options: toggleReligion(religionListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    religionListbox.bind('<<ListboxSelect>>', lambda event, listbox=religionListbox: selectReligion(listbox, options, toggleCheckbutton))

    description = tk.Frame(tab1, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a religion will swipe left\non all profiles identifying as that religion", font=('Symphonie Grotesque', 13), fg="white", bg=bg, justify='left').pack(pady=(15, 0))