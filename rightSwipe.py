import time

def profileRightSwipe(driver):
    time.sleep(0.25)
    pillButtons = driver.find_element_by_class_name("profile-userinfo-buttons")
    likeButton = pillButtons.find_element_by_id("like-button")
    likeButton.click()
    time.sleep(0.25)
    # return to discover
    driver.get("https://www.okcupid.com/discover")

def cardDeckRightSwipe(driver):
    time.sleep(0.25)
    likeButton = driver.find_element_by_class_name("pill-button.likes-pill-button.doubletake-like-button")
    likeButton.click()