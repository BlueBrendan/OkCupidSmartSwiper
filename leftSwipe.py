import time

def leftSwipe(driver):
    time.sleep(0.5)
    pillButtons = driver.find_element_by_class_name("profile-userinfo-buttons")
    passButton = pillButtons.find_element_by_id("pass-button")
    passButton.click()