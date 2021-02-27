from rightSwipe import rightSwipe
from leftSwipe import profileLeftSwipe, cardDeckLeftSwipe
from externalDisplays import updateResultsDisplay, createFinalDisplay
import time

def waitForCardDeck(driver, value):
    time.sleep(0.25)
    try:
        driver.find_element_by_class_name("cardsummary")
        value = False
        return value
    except:
        try:
            driver.find_element_by_class_name('quickmatch-blank')
            value = True
            return value
        except:
            value = waitForCardDeck(driver, value)
    return value

def waitForProfile(driver):
    time.sleep(0.25)
    try:
        driver.find_element_by_class_name('profile-basics-asl-match')
        return
    except:
        waitForProfile(driver)

def swipe(driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, totalSwipeCount, rightSwipeCount, leftSwipeCount, swipeList):
    empty = waitForCardDeck(driver, False)
    if empty:
        driver.quit()
        resultsDisplay.destroy()
        createFinalDisplay(totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList, empty)
    else:
        # check compatibility percentage
        matchPercentage = driver.find_element_by_class_name('cardsummary-item.cardsummary-match').text
        if matchPercentage[2] == '%':
            matchPercentage = int(matchPercentage[0:2])
        else:
            matchPercentage = 100

        # check number of photos
        imageElements = driver.find_elements_by_class_name('carouselimg-report')
        imageCount = len(imageElements)

        # check bio word count
        bioElements = driver.find_elements_by_class_name('qmessays-essay')
        wordCount = 0
        for i in range(len(bioElements)):
            if len(bioElements[i].text) > 0:
                wordCount += (bioElements[i].text.count(' ') + 1)

        if not (matchPercentage >= options['Minimum Percentage'].get() and imageCount >= options['Minimum Number of Images'].get() and wordCount >= options['Minimum Word Count'].get()):
            cardDeckLeftSwipe(driver)
            leftSwipeCount += 1
        else:
            # view profile to access questions
            profileLink = driver.find_element_by_class_name('cardsummary-item.cardsummary-profile-link')
            link = str(profileLink.get_attribute('innerHTML'))
            link = "https://www.okcupid.com" + link[link.index('href="') + 6:link.index('>', link.index('href="')) - 1]
            driver.get(link)
            waitForProfile(driver)

            # check number of questions answered
            questions = driver.find_elements_by_class_name("profile-questions-filter-count")
            questionCount = 0
            for i in range(len(questions)):
                if questions[i].text != ' ':
                    questionCount += int(questions[i].text.replace(',', ''))

            if questionCount >= options['Minimum Questions Answered'].get():
                name = driver.find_element_by_class_name("profile-basics-username").text
                swipeList.append([name, matchPercentage, imageCount, questionCount, link])
                rightSwipe(driver)
                rightSwipeCount+=1
            else:
                profileLeftSwipe(driver)
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
            createFinalDisplay(totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList, empty)