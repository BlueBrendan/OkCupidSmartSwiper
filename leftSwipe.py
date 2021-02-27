import time

def profileLeftSwipe(driver):
    time.sleep(0.5)
    pillButtons = driver.find_element_by_class_name("profile-userinfo-buttons")
    passButton = pillButtons.find_element_by_id("pass-button")
    passButton.click()

def cardDeckLeftSwipe(driver):
    time.sleep(0.5)
    passButton = driver.find_element_by_class_name("pill-button.pass-pill-button.doubletake-pass-button")
    passButton.click()