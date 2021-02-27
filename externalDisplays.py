import tkinter as tk

bg = "#282f3b"
secondary_bg = "#ff4ec0"
def createResultsDisplay(options):
    resultsDisplay = tk.Toplevel()
    resultsDisplay.title("Progress Window")
    resultsDisplay.configure(bg=bg)
    resultsDisplay.geometry("600x150+0+0")

    titleFrame = tk.Frame(resultsDisplay, bg=bg)
    titleFrame.pack(fill='x', pady=(20, 0))
    resultsFrame = tk.Frame(resultsDisplay, bg=bg)
    resultsFrame.pack(pady=(20,0))
    titleLabel = tk.Label()
    leftLabel = tk.Label()
    rightLabel = tk.Label()
    for index, item in enumerate(resultsDisplay.winfo_children()):
        if index == 0:
            titleLabel = tk.Label(item, text="0 out of " + str(options["Number of Swipes"].get()) + " Swipes", font=('Symphonie Grotesque', 25), fg="white", bg=bg)
            titleLabel.pack(pady=(15, 0))
        else:
            leftLabel = tk.Label(item, text="Left Swipes: 0", font=('Symphonie Grotesque', 13), fg="white", bg=bg)
            leftLabel.pack(side="left", padx=(0, 20))
            rightLabel = tk.Label(item, text="Right Swipes: 0", font=('Symphonie Grotesque', 13), fg="white", bg=bg)
            rightLabel.pack(side="right", padx=(20, 0))
    return resultsDisplay, titleLabel, leftLabel, rightLabel

def updateResultsDisplay(options, titleLabel, leftLabel, rightLabel, totalSwipeCount, leftSwipeCount, rightSwipeCount):
    titleLabel.configure(text=str(totalSwipeCount) + " out of " + str(options["Number of Swipes"].get()))
    leftLabel.configure(text="Left Swipes: " + str(leftSwipeCount))
    rightLabel.configure(text="Right Swipes: " + str(rightSwipeCount))

def createFinalDisplay(totalSwipeCount, leftSwipeCount, rightSwipeCount):
    finalDisplay = tk.Toplevel()
    finalDisplay.title("Final Results")
    finalDisplay.configure(bg=bg)
    ws = finalDisplay.winfo_screenwidth()  # width of the screen
    hs = finalDisplay.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (700 / 2)
    y = (hs / 2) - (400 / 2)
    finalDisplay.geometry('%dx%d+%d+%d' % (700, 400, x, y))

    titleFrame = tk.Frame(finalDisplay, bg=bg)
    titleFrame.pack(fill='x', pady=(20, 0))
    resultsFrame = tk.Frame(finalDisplay, bg=bg)
    resultsFrame.pack(pady=(20, 0))
    tableFrame = tk.Frame(finalDisplay, bg=bg)
    tableFrame.pack(pady=(20, 0))
    bottomFrame = tk.Frame(finalDisplay, bg=bg)
    bottomFrame.pack(pady=(20, 0))
    if totalSwipeCount == 1:
        tk.Label(titleFrame, text=str(totalSwipeCount) + " Swipe Completed", font=('Symphonie Grotesque', 25), fg="white", bg=bg).pack(pady=(20, 0))
    else:
        tk.Label(titleFrame, text=str(totalSwipeCount) + " Swipes Completed", font=('Symphonie Grotesque', 25), fg="white", bg=bg).pack(pady=(20, 0))
    tk.Label(resultsFrame, text="Left Swipes: " + str(leftSwipeCount), font=('Symphonie Grotesque', 15), fg="white", bg=bg).pack(side="left", padx=(0, 25))
    tk.Label(resultsFrame, text="Right Swipes: " + str(rightSwipeCount), font=('Symphonie Grotesque', 15), fg="white", bg=bg).pack(side="right", padx=(25, 0))
    tk.Button(bottomFrame, text="OK", command=lambda: finalDisplay.destroy(), font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack()
    finalDisplay.update()
