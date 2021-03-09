from swipe import profileRightSwipe, cardDeckRightSwipe, profileLeftSwipe, cardDeckLeftSwipe
from externalDisplays import updateResultsDisplay, createFinalDisplay
import time

def waitForCardDeck(driver, value):
    time.sleep(0.3)
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
        driver.find_elements_by_class_name("profile-questions-filter-count")
        return
    except:
        waitForProfile(driver)

def inspectProfileFunction(root, driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, totalSwipeCount, rightSwipeCount, leftSwipeCount, swipeList, buttons):
    empty = waitForCardDeck(driver, False)
    if empty:
        createFinalDisplay(root, totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList, resultsDisplay, titleLabel, leftLabel, rightLabel, empty, buttons, options, driver)
    elif totalSwipeCount >= options['Number of Swipes'].get():
        createFinalDisplay(root, totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList, resultsDisplay, titleLabel, leftLabel, rightLabel, empty, buttons, options, driver)
    else:
        # check compatibility percentage
        matchPercentage = driver.find_element_by_class_name('cardsummary-item.cardsummary-match').text
        if matchPercentage[2] == '%':
            matchPercentage = int(matchPercentage[0:2])
        else:
            matchPercentage = 100

        # check number of photos
        imageElements = driver.find_elements_by_class_name('fadein-image.image_wrapper.loaded')
        imageCount = len(imageElements)

        # check bio word count and content
        bioElements = driver.find_elements_by_class_name('qmessays-essay')
        wordCount = 0
        phrasePass = False
        for i in range(len(bioElements)):
            passage = bioElements[i].find_element_by_css_selector('p').text
            if len(passage) > 0:
                wordCount += (passage.count(' ') + 1)
            for phrase in options['Phrases']:
                if phrase.lower() in passage.lower():
                    phrasePass = True
                    break

        # check orientation (if applicable)
        orientationPass = False
        try:
            orientationDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--basics').text)
            for orientation in options['Orientations']:
                if orientation.lower() in orientationDescription.lower():
                    orientationPass = True
                    break
        except:
            pass

        # check body type (if applicable)
        bodyTypePass = False
        try:
            bodyTypeDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--looks').text)
            for bodyType in options['Body Types']:
                if bodyType.lower() in bodyTypeDescription.lower():
                    bodyTypePass = True
                    break
        except:
            pass

        # check ethnicity (if applicable)
        ethnicityPass = False
        try:
            if not bodyTypePass:
                ethnicityDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--background').text)
                for ethnicity in options['Ethnicities']:
                    if ethnicity.lower() in ethnicityDescription.lower():
                        ethnicityPass = True
                        break
        except:
            pass

        # check for intro
        intro = False
        try:
            driver.find_element_by_id('firstmessage2017')
            intro = True
        except:
            pass

        if options['Check Intro'].get() and intro:
            cardDeckRightSwipe(driver)
            rightSwipeCount += 1
        elif orientationPass or bodyTypePass or ethnicityPass or phrasePass:
            cardDeckLeftSwipe(driver)
            leftSwipeCount += 1
        elif options['Check Percentage'].get() and not matchPercentage >= options['Minimum Percentage'].get():
            cardDeckLeftSwipe(driver)
            leftSwipeCount += 1
        elif options['Check Images'].get() and not imageCount >= options['Minimum Number of Images'].get():
            cardDeckLeftSwipe(driver)
            leftSwipeCount += 1
        elif options['Check Words'].get() and not wordCount >= options['Minimum Word Count'].get():
            cardDeckLeftSwipe(driver)
            leftSwipeCount += 1
        else:
            # swipe right if questions check is disabled
            if not options['Check Questions'].get():
                name = driver.find_element_by_class_name("cardsummary-item.cardsummary-realname").text
                profileLink = driver.find_element_by_class_name('cardsummary-item.cardsummary-profile-link')
                link = str(profileLink.get_attribute('innerHTML'))
                link = "https://www.okcupid.com" + link[link.index('href="') + 6:link.index('>', link.index('href="')) - 1]
                swipeList.append([name, matchPercentage, imageCount, wordCount, 'NA', link])
                cardDeckRightSwipe(driver)
                rightSwipeCount += 1
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
                    swipeList.append([name, matchPercentage, imageCount, wordCount, questionCount, link])
                    profileRightSwipe(driver)
                    rightSwipeCount+=1
                else:
                    profileLeftSwipe(driver)
                    leftSwipeCount+=1
        totalSwipeCount+=1
        # update results display
        updateResultsDisplay(options, titleLabel, leftLabel, rightLabel, totalSwipeCount, leftSwipeCount, rightSwipeCount)
        resultsDisplay.update()
        inspectProfileFunction(root, driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, totalSwipeCount, rightSwipeCount, leftSwipeCount, swipeList, buttons)