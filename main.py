from selenium import webdriver
import time
from login import login
from resourcePath import resourcePath
import tkinter as tk

# launch OkCupid
bg = "#282f3b"
secondary_bg = "#ff4ec0"
root = tk.Tk()
root.title("OkCupid Smart Swipe")
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (800/2)
y = (hs/2) - (400/2)
root.geometry('%dx%d+%d+%d' % (800, 400, x, y))
root.configure(bg=bg)


mainContainer = tk.Frame(root, bg=bg)
mainContainer.pack()

title = tk.Label(mainContainer, text="OkCupid Smart Swipe", font=('Symphonie Grotesque', 45), fg="white", bg=bg).pack(pady=(30, 0))
optionsTopRow = tk.Frame(mainContainer, bg=bg)
optionsTopRow.pack(pady=(40, 0))
# compatibility percentage threshold selection
compatibilityContainer = tk.Frame(optionsTopRow, bg=bg)
compatibilityContainer.pack(side="left")
compatibilityContainerTitle = tk.Label(compatibilityContainer, text="Minimum Compatibility\nPercentage", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
percentage = tk.StringVar(value="95")
compatibilityEntry = tk.Entry(compatibilityContainer, width=5, textvariable=percentage, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black", highlightcolor="grey", selectbackground=bg).pack(anchor="w", padx=(3, 0))

# number of images threshold selection
imagesContainer = tk.Frame(optionsTopRow, bg=bg)
imagesContainer.pack(side="left", padx=(30, 0))
imagesContainerTitle = tk.Label(imagesContainer, text="Minimum Number\nof Images", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
images = tk.StringVar(value="3")
imagesContainerEntry = tk.Entry(imagesContainer, width=5, textvariable=images, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black", highlightcolor="grey", selectbackground=bg).pack(anchor="w", padx=(3, 0))

# number of words threshold selection
wordsContainer = tk.Frame(optionsTopRow, bg=bg)
wordsContainer.pack(side="left", padx=(30, 0))
wordsContainerTitle = tk.Label(wordsContainer, text="Minimum Word\nCount in Bio", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
words = tk.StringVar(value="20")
wordsContainerEntry = tk.Entry(wordsContainer, width=5, textvariable=words, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black", highlightcolor="grey", selectbackground=bg).pack(anchor="w", padx=(3, 0))

# number of questions threshold selection
questionsContainer = tk.Frame(optionsTopRow, bg=bg)
questionsContainer.pack(side="left", padx=(30, 0))
questionsContainerTitle = tk.Label(questionsContainer, text="Minimum Number\nof Questions Answered", font=('Symphonie Grotesque', 14), fg="white", justify="left", bg=bg).pack()
questions = tk.StringVar(value="50")
questionsContainerEntry = tk.Entry(questionsContainer, width=5, textvariable=questions, validate="key", font=("Proxima Nova Rg", 11), highlightbackground="black", highlightcolor="grey", selectbackground=bg).pack(anchor="w", padx=(3, 0))

startButton = tk.Button(mainContainer, text="BEGIN SWIPING", font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(50, 0))
bottomText = tk.Label(mainContainer, text="OkCupid Smart Swipe exists solely to enhance the swiping experience and is completely unaffiliated with OkCupid", font=('Symphonie Grotesque', 10), fg="white", bg=bg, highlightthickness=0).pack(pady=(70, 0))
root.mainloop()
# driver = webdriver.Chrome(executable_path=resourcePath('chromedriver'))
# driver.get("https://www.okcupid.com/home")

# check if user is logged in
# time.sleep(2)
# text = driver.find_elements_by_class_name("OkModalContent.reactmodal.signin-modal.login-modal.login-modal-icon-cross")
# if len(text) > 0:
#     login(driver)
# check compatibility percentage
# check number of photos
# check bio word count
# check number of questions answered

