from rightSwipe import rightSwipe
from leftSwipe import leftSwipe
from externalDisplays import updateResultsDisplay, createFinalDisplay
import time

def waitForCardDeck(driver):
    time.sleep(1)
    try:
        driver.find_element_by_class_name("cardsummary")
        return
    except:
        waitForCardDeck(driver)

def waitForProfile(driver):
    time.sleep(1)
    try:
        driver.find_element_by_class_name('profile-basics-asl-match')
        return
    except:
        waitForProfile(driver)

def swipe(driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, totalSwipeCount, rightSwipeCount, leftSwipeCount, swipeList):
    time.sleep(1)
    waitForCardDeck(driver)
    profileLink = driver.find_element_by_class_name('cardsummary-item.cardsummary-profile-link')
    link = str(profileLink.get_attribute('innerHTML'))
    link = "https://www.okcupid.com" + link[link.index('href="') + 6:link.index('>', link.index('href="')) - 1]
    driver.get(link)
    time.sleep(1)
    waitForProfile(driver)

    # check compatibility percentage
    matchPercentage = driver.find_element_by_class_name('profile-basics-asl-match').text
    if matchPercentage[2] == '%':
        matchPercentage = int(matchPercentage[0:2])
    else:
        matchPercentage = 100

    # check number of photos
    imageElement = driver.find_element_by_class_name('profile-thumb')
    imageCount = len(imageElement.find_elements_by_tag_name('img'))

    # press "More" button to reveal full bio (if applicable)
    try:
        moreButton = driver.find_element_by_xpath("//button[@class='profile-essays-expander']")
        moreButton.click()
    except:
        pass

    # check bio word count
    bioElements = driver.find_elements_by_class_name('profile-essay-contents')
    wordCount = 0
    for i in range(len(bioElements)):
        if len(bioElements[i].text) > 0: wordCount += (bioElements[i].text.count(' ') + 1)

    # check number of questions answered
    questions = driver.find_elements_by_class_name("profile-questions-filter-count")
    questionCount = 0
    for i in range(len(questions)):
        if questions[i].text != ' ':
            questionCount += int(questions[i].text.replace(',', ''))

    if matchPercentage >= options['Minimum Percentage'].get() and imageCount >= options['Minimum Number of Images'].get() and wordCount >= options['Minimum Word Count'].get() and questionCount >= options['Minimum Questions Answered'].get():
        name = driver.find_element_by_class_name("profile-basics-username").text
        swipeList.append([name, matchPercentage, imageCount, questionCount, link])
        rightSwipe(driver)
        rightSwipeCount+=1
    else:
        leftSwipe(driver)
        leftSwipeCount+=1
    totalSwipeCount+=1
    # update results display
    updateResultsDisplay(options, titleLabel, leftLabel, rightLabel, totalSwipeCount, leftSwipeCount, rightSwipeCount)
    resultsDisplay.update()
    if totalSwipeCount < options['Number of Swipes'].get():
        swipe(driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, totalSwipeCount, rightSwipeCount, leftSwipeCount, swipeList)
    else:
        driver.quit()
        resultsDisplay.destroy()
        createFinalDisplay(totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList)