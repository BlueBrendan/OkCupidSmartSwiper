from settings import resourcePath
import tkinter as tk
from sys import platform

invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectEthnicity(listbox, options, toggleCheckbutton):
    index = int(listbox.curselection()[0])
    toggleCheckbutton.config(state=tk.NORMAL)
    if listbox.get(index) in options['Ethnicities']:
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
        toggleCheckbutton.deselect()
    else:
        toggleCheckbutton.select()

def toggleEthnicity(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalEthnicities = 'Ethnicities:'
    for ethnicity in options['Ethnicities']:
        originalEthnicities += ethnicity + ','
    if originalEthnicities[-1] == ',': originalEthnicities = originalEthnicities[:-1]
    if listbox.get(index) not in options['Ethnicities']:
        options['Ethnicities'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Ethnicities'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newEthnicities = 'Ethnicities:'
    for ethnicity in options['Ethnicities']:
        newEthnicities += ethnicity + ','
    if newEthnicities[-1] == ',': newEthnicities = newEthnicities[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalEthnicities), str(newEthnicities)))

def onClose(button, window):
    button.config(state=tk.NORMAL)
    window.destroy()

def ethnicityEdit(options, button, bg, secondary_bg, tertiary_bg):
    # disable body type button until window is closed
    button.config(state=tk.DISABLED)
    quaternary_bg = "#2f3346"
    ethnicityWindow = tk.Toplevel()
    ethnicityWindow.title("Ethnicity Preferences")
    ws = ethnicityWindow.winfo_screenwidth()  # width of the screen
    hs = ethnicityWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (400 / 2)
    ethnicityWindow.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    ethnicityWindow.configure(bg=bg)
    if platform == 'win32':
        ethnicityWindow.iconbitmap(resourcePath('favicon.ico'))
    listboxContainer = tk.Frame(ethnicityWindow, bg=bg)
    listboxContainer.pack()
    ethnicityListbox = tk.Listbox(listboxContainer,  font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg,  highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    ethnicities = ['Asian', 'Black', 'Hispanic/Latin', 'Indian', 'Middle Eastern', 'Native American', 'Pacific Islander', 'White', 'Other']
    for index, ethnicity in enumerate(ethnicities):
        ethnicityListbox.insert(tk.END, ethnicity)
        if ethnicity in options['Ethnicities']:
            ethnicityListbox.itemconfig(index, bg=invalid_color)
    ethnicityListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=ethnicityListbox,options=options: toggleEthnicity(ethnicityListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    ethnicityListbox.bind('<<ListboxSelect>>', lambda event, listbox=ethnicityListbox: selectEthnicity(listbox, options, toggleCheckbutton))

    description = tk.Frame(ethnicityWindow, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling an ethnicity will swipe left\non all profiles identifying as that ethnicity", font=('Symphonie Grotesque', 15), fg="white", bg=bg, justify='left').pack(pady=(15, 0))

    ethnicityWindow.protocol("WM_DELETE_WINDOW", lambda button=button, window=ethnicityWindow: onClose(button, window))