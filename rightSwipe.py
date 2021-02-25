import time

def rightSwipe(driver):
    likeButton = driver.find_element_by_id("like-button")
    likeButton.click()