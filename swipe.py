import time

def profileLeftSwipe(driver):
    time.sleep(0.25)
    pillButtons = driver.find_element_by_class_name("profile-userinfo-buttons")
    passButton = pillButtons.find_element_by_id("pass-button")
    passButton.click()

def profileRightSwipe(driver):
    time.sleep(0.25)
    pillButtons = driver.find_element_by_class_name("profile-userinfo-buttons")
    likeButton = pillButtons.find_element_by_id("like-button")
    likeButton.click()
    time.sleep(0.25)
    # return to discover
    driver.get("https://www.okcupid.com/discover")

def cardDeckLeftSwipe(driver):
    time.sleep(0.25)
    passButton = driver.find_element_by_class_name("pill-button.pass-pill-button.doubletake-pass-button")
    passButton.click()

def cardDeckRightSwipe(driver):
    time.sleep(0.25)
    likeButton = driver.find_element_by_class_name("pill-button.likes-pill-button.doubletake-like-button")
    likeButton.click()