from selenium import webdriver
from inspectUserProfile import inspectProfileFunction
from externalDisplays import createResultsDisplay
from settings import readConfigFile, createConfigFile, resourcePath
from sys import platform
import tkinter as tk
import time
import os

def waitForLogin(driver, bg, secondary_bg):
    time.sleep(0.25)
    try:
        driver.find_element_by_id("username")
        loginScreen(driver, bg, secondary_bg)
        return
    except:
        try:
            driver.find_element_by_class_name("cardsummary")
            pass
        except:
            waitForLogin(driver, bg, secondary_bg)

# launch OkCupid
def login(root, buttons, bg, secondary_bg):
    # disable all menu button until completion
    for button in buttons:
        button.config(state=tk.DISABLED)

    # retrieve user settings
    if not os.path.exists(resourcePath('Settings.txt')):
        createConfigFile(bg, secondary_bg)
    options = readConfigFile(bg, secondary_bg)

    # open selenium (MacOS currently not supported)
    if platform == 'win32':
        driver = webdriver.Firefox(executable_path=resourcePath('geckodriver.exe'))
    else:
        driver = webdriver.Firefox(executable_path=resourcePath('geckodriver'))
    driver.maximize_window()
    driver.get("https://www.okcupid.com/home")
    waitForLogin(driver, bg, secondary_bg)

    resultsDisplay, titleLabel, leftLabel, rightLabel = createResultsDisplay(options)
    resultsDisplay.update()
    inspectProfileFunction(root, driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, 0, 0, 0, [], buttons)

def loginScreen(driver, bg, secondary_bg):
    loginScreenWindow = tk.Toplevel()
    loginScreenWindow.title("Login Popup")
    loginScreenWindow.configure(bg=bg)
    loginScreenWindow.geometry("600x200+0+0")
    loginScreenWindow.attributes("-topmost", 1)
    if platform == 'win32':
        loginScreenWindow.iconbitmap(resourcePath('favicon.ico'))
    infoFrame = tk.Frame(loginScreenWindow, bg=bg)
    infoFrame.pack(fill='x', pady=(15, 0))
    tk.Label(infoFrame, text="The login screen has been detected. Enter your credentials and press the button below once you have reached the OkCupid homepage\n\nThis is required once per session because Selenium does not save user data", wraplength=550, bg=bg, font=('Symphonie Grotesque', 13), fg="white").pack(pady=(10, 0))
    tk.Button(infoFrame, command=lambda: checkForCards(driver, loginScreenWindow, bg, secondary_bg), text="I'VE REACHED THE HOMESCREEN", font=('Symphonie Grotesque', 15), fg="white", bg=secondary_bg, highlightthickness=0, activebackground=secondary_bg, activeforeground="white").pack(pady=(30, 0))
    loginScreenWindow.protocol('WM_DELETE_WINDOW', lambda: checkForCards(driver, loginScreenWindow, bg, secondary_bg))
    loginScreenWindow.wait_window()

def checkForCards(driver, phoneLoginScreen, bg, secondary_bg):
    try:
        phoneLoginScreen.destroy()
        driver.find_element_by_class_name('OkModalContent.reactmodal.signin-modal.login-modal.login-modal-icon-cross')
        loginScreen(driver, bg, secondary_bg)
    except:
        pass


