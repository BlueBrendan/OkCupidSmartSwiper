from settings import resourcePath
import tkinter as tk
from tkinter import ttk
from basicsTabs.orientationTab import orientationEdit
from basicsTabs.relationshipTab import relationshipEdit
from sys import platform

invalid_color = '#801212'
invalid_selection = '#9c1616'

def onClose(button, window):
    button.config(state=tk.NORMAL)
    window.destroy()

def basicsEdit(options, button, bg, secondary_bg, tertiary_bg):
    # disable body type button until window is closed
    button.config(state=tk.DISABLED)

    basicsWindow = tk.Toplevel()
    basicsWindow.title("Basics Preferences")
    ws = basicsWindow.winfo_screenwidth()  # width of the screen
    hs = basicsWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (400 / 2)
    basicsWindow.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    basicsWindow.configure(bg=bg)
    if platform == 'win32':
        basicsWindow.iconbitmap(resourcePath('favicon.ico'))

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

    tab_parent = ttk.Notebook(basicsWindow)
    tab_parent.pack(expand=1, fill='both')

    orientationEdit(tab_parent, options)
    relationshipEdit(tab_parent, options)

    basicsWindow.protocol("WM_DELETE_WINDOW", lambda button=button, window=basicsWindow: onClose(button, window))