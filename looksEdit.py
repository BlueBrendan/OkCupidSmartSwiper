from settings import resourcePath
import tkinter as tk
from tkinter import ttk
from looksTabs.bodyTab import bodyEdit
from sys import platform

invalid_color = '#801212'
invalid_selection = '#9c1616'

def onClose(button, window):
    button.config(state=tk.NORMAL)
    window.destroy()

def looksEdit(options, button, bg, secondary_bg, tertiary_bg):
    # disable body type button until window is closed
    button.config(state=tk.DISABLED)

    looksWindow = tk.Toplevel()
    looksWindow.title("Looks Preferences")
    ws = looksWindow.winfo_screenwidth()  # width of the screen
    hs = looksWindow.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (500 / 2)
    y = (hs / 2) - (400 / 2)
    looksWindow.geometry('%dx%d+%d+%d' % (500, 400, x, y))
    looksWindow.configure(bg=bg)
    if platform == 'win32':
        looksWindow.iconbitmap(resourcePath('favicon.ico'))

    s = ttk.Style()
    try:
        s.theme_create("Smart Swiper", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], "background": bg, 'borderwidth': 0}},
            "TNotebook.Tab": {
                "configure": {"padding": [13, 5], "font": ('Symphonie Grotesque', '13'), "background": tertiary_bg, 'foreground': 'white', 'borderwidth': 1},
                "map": {"background": [("selected", bg)], "expand": [("selected", [1, 1, 1, 0])]}}})
    except:
        pass
    s.theme_use("Smart Swiper")

    tab_parent = ttk.Notebook(looksWindow)
    tab_parent.pack(expand=1, fill='both')

    bodyEdit(tab_parent, options)

    looksWindow.protocol("WM_DELETE_WINDOW", lambda button=button, window=looksWindow: onClose(button, window))