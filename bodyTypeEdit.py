from resourcePath import resourcePath
import tkinter as tk

invalid_color = '#801212'
invalid_selection = '#9c1616'

def selectBodyType(listbox, options, toggleCheckbutton):
    index = int(listbox.curselection()[0])
    toggleCheckbutton.config(state=tk.NORMAL)
    if listbox.get(index) in options['Body Types']:
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
        toggleCheckbutton.deselect()
    else:
        toggleCheckbutton.select()

def toggleBodyType(listbox, options, tertiary_bg, quaternary_bg):
    index = int(listbox.curselection()[0])
    originalBodyTypes = 'Body Types:'
    for type in options['Body Types']:
        originalBodyTypes += type + ','
    if originalBodyTypes[-1] == ',': originalBodyTypes = originalBodyTypes[:-1]
    if listbox.get(index) not in options['Body Types']:
        options['Body Types'].append(listbox.get(index))
        listbox.itemconfig(index, bg=invalid_color, selectbackground=invalid_selection)
    else:
        options['Body Types'].remove(listbox.get(index))
        listbox.itemconfig(index, bg=quaternary_bg, selectbackground=tertiary_bg)
    # write to settings file
    CONFIG_FILE = open(resourcePath('Settings.txt'), 'r').read()
    newBodyTypes = 'Body Types:'
    for type in options['Body Types']:
        newBodyTypes += type + ','
    if newBodyTypes[-1] == ',': newBodyTypes = newBodyTypes[:-1]
    with open(resourcePath('Settings.txt'), 'wt') as file:
        file.write(CONFIG_FILE.replace(str(originalBodyTypes), str(newBodyTypes)))

def onClose(button, window):
    button.config(state=tk.NORMAL)
    window.destroy()

def bodyTypeEdit(options, button, bg, secondary_bg, tertiary_bg):
    # disable body type button until window is closed
    button.config(state=tk.DISABLED)
    quaternary_bg = "#2f3346"
    bodyTypeWindow = tk.Toplevel()
    bodyTypeWindow.title("Body Type Preferences")
    ws = bodyTypeWindow.winfo_screenwidth()  # width of the screen
    hs = bodyTypeWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (400 / 2)
    bodyTypeWindow.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    bodyTypeWindow.configure(bg=bg)

    listboxContainer = tk.Frame(bodyTypeWindow, bg=bg)
    listboxContainer.pack()
    bodyTypeListbox = tk.Listbox(listboxContainer,  font=('Symphonie Grotesque', 15), bg=quaternary_bg, selectbackground=tertiary_bg, highlightbackground=quaternary_bg,  highlightcolor=quaternary_bg, fg='white', selectforeground='white', activestyle='none')
    bodyTypes = ['Thin', 'Average', 'Fit', 'Jacked', 'A little extra', 'Overweight', 'Curvy', 'Fully Figured']
    for index, bodyType in enumerate(bodyTypes):
        bodyTypeListbox.insert(tk.END, bodyType)
        if bodyType in options['Body Types']:
            bodyTypeListbox.itemconfig(index, bg=invalid_color)
    bodyTypeListbox.pack(pady=(30, 0))
    toggleCheckbutton = tk.Checkbutton(listboxContainer, command=lambda listbox=bodyTypeListbox,options=options: toggleBodyType(bodyTypeListbox, options, tertiary_bg, quaternary_bg), bg=bg, highlightbackground=bg, activebackground=bg, state=tk.DISABLED)
    toggleCheckbutton.select()
    toggleCheckbutton.pack(pady=(5, 0))
    bodyTypeListbox.bind('<<ListboxSelect>>', lambda event, listbox=bodyTypeListbox: selectBodyType(listbox, options, toggleCheckbutton))

    description = tk.Frame(bodyTypeWindow, bg=bg)
    description.pack()
    tk.Label(description, text="Disabling a body type will swipe left\non all profiles identifying as that body type", font=('Symphonie Grotesque', 15), fg="white", bg=bg, justify='left').pack(pady=(15, 0))

    bodyTypeWindow.protocol("WM_DELETE_WINDOW", lambda button=button, bodyTypeWindow=bodyTypeWindow: onClose(button, bodyTypeWindow))