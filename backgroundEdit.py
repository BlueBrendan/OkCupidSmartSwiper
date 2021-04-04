from settings import resourcePath
import tkinter as tk
from tkinter import ttk
from backgroundTabs.ethnicityTab import ethnicityEdit
from backgroundTabs.religionTab import religionEdit
from backgroundTabs.educationTab import educationEdit
from sys import platform

invalid_color = '#801212'
invalid_selection = '#9c1616'

def onClose(button, window):
    button.config(state=tk.NORMAL)
    window.destroy()

def backgroundEdit(options, button, bg, secondary_bg, tertiary_bg):
    # disable body type button until window is closed
    button.config(state=tk.DISABLED)

    backgroundWindow = tk.Toplevel()
    backgroundWindow.title("Background Preferences")
    ws = backgroundWindow.winfo_screenwidth()  # width of the screen
    hs = backgroundWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (400 / 2)
    backgroundWindow.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    backgroundWindow.configure(bg=bg)
    if platform == 'win32':
        backgroundWindow.iconbitmap(resourcePath('favicon.ico'))

    s = ttk.Style()
    try:
        s.theme_create("Smart Swiper", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], "background": bg, 'borderwidth': 0}},
            "TNotebook.Tab": {
                "configure": {"padding": [13, 5], "font": ('Symphonie Grotesque', '14'), "background": tertiary_bg, 'foreground': 'white', 'borderwidth': 1},
                "map": {"background": [("selected", bg)], "expand": [("selected", [1, 1, 1, 0])]}}})
    except:
        pass
    s.theme_use("Smart Swiper")

    tab_parent = ttk.Notebook(backgroundWindow)
    tab_parent.pack(expand=1, fill='both')

    ethnicityEdit(tab_parent, options)
    religionEdit(tab_parent, options)
    educationEdit(tab_parent, options)

    backgroundWindow.protocol("WM_DELETE_WINDOW", lambda button=button, window=backgroundWindow: onClose(button, window))