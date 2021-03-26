import tkinter as tk
from sys import platform
from tkinter import ttk
from settings import resourcePath
import webbrowser

bg = "#282f3b"
secondary_bg = "#ff4ec0"
tertiary_bg = "#2f3346"

def createResultsDisplay(options):
    resultsDisplay = tk.Toplevel()
    resultsDisplay.title("Progress Window")
    resultsDisplay.configure(bg=bg)
    resultsDisplay.geometry("600x180+0+0")
    if platform == 'win32':
        resultsDisplay.iconbitmap(resourcePath('favicon.ico'))
    resultsDisplay.attributes("-topmost", 1)
    titleFrame = tk.Frame(resultsDisplay, bg=bg)
    titleFrame.pack(fill='x', pady=(20, 0))
    resultsFrame = tk.Frame(resultsDisplay, bg=bg)
    resultsFrame.pack(pady=(20,0))
    titleLabel = tk.Label()
    leftLabel = tk.Label()
    rightLabel = tk.Label()
    for index, item in enumerate(resultsDisplay.winfo_children()):
        if index == 0:
            titleLabel = tk.Label(item, text="0 out of " + str(options["Number of Swipes"].get()), font=('Symphonie Grotesque', 25), fg="white", bg=bg)
            titleLabel.pack(pady=(15, 10))
        else:
            leftLabel = tk.Label(item, text="Left Swipes: 0", font=('Symphonie Grotesque', 13), fg="white", bg=bg)
            leftLabel.pack(side="left", padx=(0, 20))
            if options['Check Criteria'].get():
               rightLabel = tk.Label(item, text="Right Swipes: 0", font=('Symphonie Grotesque', 13), fg="white", bg=bg)
            else:
                rightLabel = tk.Label(item, text="Potential Swipes: 0", font=('Symphonie Grotesque', 13), fg="white", bg=bg)
            rightLabel.pack(side="right", padx=(20, 0))
    return resultsDisplay, titleLabel, leftLabel, rightLabel

def updateResultsDisplay(options, titleLabel, leftLabel, rightLabel, totalSwipeCount, leftSwipeCount, rightSwipeCount):
    titleLabel.configure(text=str(totalSwipeCount) + " out of " + str(options["Number of Swipes"].get()))
    leftLabel.configure(text="Left Swipes: " + str(leftSwipeCount))
    if options['Check Criteria'].get():
        rightLabel.configure(text="Right Swipes: " + str(rightSwipeCount))
    else:
        rightLabel.configure(text="Potential Swipes: " + str(rightSwipeCount))

def openProfile(rightSwipeListbox, swipeList):
    webbrowser.open_new(swipeList[int(rightSwipeListbox.focus())][5])

def closeWindow(root, window, buttons, driver):
    window.destroy()
    for button in buttons:
        button.config(state=tk.NORMAL)
    driver.quit()
    root.attributes("-topmost", 1)
    root.attributes("-topmost", 0)

def swipeAgain(root, window, options, buttons, driver):
    window.destroy()
    resultsDisplay, titleLabel, leftLabel, rightLabel = createResultsDisplay(options)
    from inspectProfile import inspectProfileFunction
    inspectProfileFunction(root, driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, 0, 0, 0, [], buttons)

def createFinalDisplay(root, totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList, resultsDisplay, empty, buttons, options, driver):
    resultsDisplay.destroy()
    finalDisplay = tk.Toplevel()
    finalDisplay.title("Final Results")
    finalDisplay.configure(bg=bg)
    ws = finalDisplay.winfo_screenwidth()  # width of the screen
    hs = finalDisplay.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (800 / 2)
    y = (hs / 2) - (570 / 2)
    finalDisplay.geometry('%dx%d+%d+%d' % (800, 570, x, y))
    if platform == 'win32':
        finalDisplay.iconbitmap(resourcePath('favicon.ico'))
    titleFrame = tk.Frame(finalDisplay, bg=bg)
    titleFrame.pack(fill='x', pady=(20, 0))
    resultsFrame = tk.Frame(finalDisplay, bg=bg)
    resultsFrame.pack(pady=(20, 0))
    infoFrame = tk.Frame(finalDisplay, bg=bg)
    infoFrame.pack(fill='x', pady=(10, 10))
    tableFrame = tk.Frame(finalDisplay, bg=bg)
    tableFrame.pack(pady=(20, 0))
    bottomFrame = tk.Frame(finalDisplay, bg=bg)
    bottomFrame.pack(pady=(20, 0))
    if totalSwipeCount == 1:
            tk.Label(titleFrame, text=str(totalSwipeCount) + " Swipe Completed", font=('Symphonie Grotesque', 25), fg="white", bg=bg).pack(pady=(20, 0))
    else:
            tk.Label(titleFrame, text=str(totalSwipeCount) + " Swipes Completed", font=('Symphonie Grotesque', 25), fg="white", bg=bg).pack(pady=(20, 0))
    tk.Label(resultsFrame, text="Left Swipes: " + str(leftSwipeCount), font=('Symphonie Grotesque', 15), fg="white", bg=bg).pack(side="left", padx=(0, 25))
    if options['Check Criteria'].get():
        tk.Label(resultsFrame, text="Right Swipes: " + str(rightSwipeCount), font=('Symphonie Grotesque', 15), fg="white", bg=bg).pack(side="right", padx=(25, 0))
    else:
        tk.Label(resultsFrame, text="Potential Swipes: " + str(rightSwipeCount), font=('Symphonie Grotesque', 15), fg="white", bg=bg).pack(side="right", padx=(25, 0))
    if (empty):
        tk.Label(infoFrame, text="Program ended prematurely due to empty stack!\nChange your preferences to find more matches", font=('Symphonie Grotesque', 12), fg="white", bg=bg).pack(pady=(10, 0))

    # treeview to display all profiles we swiped right on
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", bd=0, font=('Symphonie Grotesque', 15), background=tertiary_bg, foreground='white',fieldbackground=bg)
    style.configure("Treeview.Heading", font=('Symphonie Grotesque', 15), background=tertiary_bg, foreground='white', fieldbackground=bg)

    rightSwipeListbox = ttk.Treeview(tableFrame, columns=("#", "Name", "Match Percentage", "Image Count", "Word Count", "Question Count"), style='Treeview')
    rightSwipeListbox.pack(pady=(20, 0))
    rightSwipeListbox.column('#0', width=0, stretch=tk.NO)
    rightSwipeListbox.column('#1', anchor=tk.CENTER, width=60)
    rightSwipeListbox.column('#2', width=120)
    rightSwipeListbox.column('#3', anchor=tk.CENTER, width=120)
    rightSwipeListbox.column('#4', anchor=tk.CENTER, width=120)
    rightSwipeListbox.column('#5', anchor=tk.CENTER, width=120)
    rightSwipeListbox.column('#6', anchor=tk.CENTER, width=120)
    rightSwipeListbox.heading('#1', text="#")
    rightSwipeListbox.heading('#2', text="Name")
    rightSwipeListbox.heading('#3', text="Match %")
    rightSwipeListbox.heading('#4', text="Images")
    rightSwipeListbox.heading('#5', text="Words")
    rightSwipeListbox.heading('#6', text="Questions")
    for i in range(len(swipeList)):
        rightSwipeListbox.bind("<Double-1>", lambda e, rightSwipeListbox=rightSwipeListbox, swipeList=swipeList: openProfile(rightSwipeListbox, swipeList))
        rightSwipeListbox.insert('', 'end', i, values=(i+1, swipeList[i][0], str(swipeList[i][1]) + '%', swipeList[i][2], swipeList[i][3],swipeList[i][4]))

    tk.Button(bottomFrame, text="OK", width=12, command=lambda finalDisplay=finalDisplay, buttons=buttons: closeWindow(root, finalDisplay, buttons, driver), font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(10, 0))
    tk.Button(bottomFrame, text="SWIPE AGAIN", width=12, command=lambda finalDisplay=finalDisplay, buttons=buttons: swipeAgain(root, finalDisplay, options, buttons, driver), font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(20, 0))
    finalDisplay.protocol("WM_DELETE_WINDOW", lambda finalDisplay=finalDisplay, buttons=buttons: closeWindow(root, finalDisplay, buttons, driver))
    finalDisplay.update()