from swipe import profileRightSwipe, cardDeckRightSwipe, profileLeftSwipe, cardDeckLeftSwipe
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
        driver.find_elements_by_class_name("profile-questions-filter-count")
        return
    except:
        waitForProfile(driver)

def waitForSection(driver, count, value, type):
    if count >= 5:
        value = False
        return value
    try:
        if type == 'basics':
            driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--basics')
        elif type == 'looks':
            driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--looks')
        elif type == 'background':
            driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--background')
        elif type == 'lifestyle':
            driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--lifestyle')
        elif type == 'family':
            driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--family')
        value = True
        return value
    except:
        try:
            driver.find_element_by_class_name('matchprofile-details-section.isLoading')
            time.sleep(0.3)
            count += 1
            waitForSection(driver, count, value, type)
        except:
            value = False
            return value
    return value

def inspectProfileFunction(root, driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, totalSwipeCount, rightSwipeCount, leftSwipeCount, swipeList, buttons):
    empty = waitForCardDeck(driver, False)
    if empty:
        createFinalDisplay(root, totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList, resultsDisplay, empty, buttons, options, driver)
    elif totalSwipeCount >= options['Number of Swipes'].get():
        createFinalDisplay(root, totalSwipeCount, leftSwipeCount, rightSwipeCount, swipeList, resultsDisplay, empty, buttons, options, driver)
    else:
        # check compatibility percentage
        matchPercentage = driver.find_element_by_class_name('cardsummary-item.cardsummary-match').text
        while matchPercentage == '':
            time.sleep(0.20)
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

        # check orientation/relationship type (if applicable)
        basicsPass = False
        value = waitForSection(driver, 0, False, 'basics')
        if value:
            basicsDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--basics').text).lower()
            for orientation in options['Orientation']:
                if orientation.lower() in basicsDescription:
                    basicsPass = True
                    break
            for relationship in options['Relationship']:
                if relationship.lower() in basicsDescription:
                    basicsPass = True
                    break

        # check body type (if applicable)
        bodyTypePass = False
        value = waitForSection(driver, 0, False, 'looks')
        if value:
            bodyTypeDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--looks').text).lower()
            for bodyType in options['Body Type']:
                if bodyType.lower() in bodyTypeDescription.lower():
                    bodyTypePass = True
                    break

        # check ethnicity/religion/education (if applicable)
        backgroundPass = False
        value = waitForSection(driver, 0, False, 'background')
        if value:
            backgroundDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--background').text).lower()
            for ethnicity in options['Ethnicity']:
                if ethnicity.lower() in backgroundDescription:
                    backgroundPass = True
                    break
            for religion in options['Religion']:
                if religion.lower() in backgroundDescription:
                    backgroundPass = True
                    break
            for education in options['Education']:
                if education.lower() in backgroundDescription:
                    backgroundPass = True
                    break

        # check cigarettes/alcohol/marijuana (if applicable)
        lifestylePass = False
        value = waitForSection(driver, 0 , False, 'lifestyle')
        if value:
            lifestyleDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--lifestyle').text).lower()
            for cigarettes in options['Cigarettes']:
                if cigarettes.lower() in lifestyleDescription:
                    lifestylePass = True
                    break
            for alcohol in options['Alcohol']:
                if alcohol.lower() in lifestyleDescription:
                    lifestylePass = True
                    break
            for marijuana in options['Marijuana']:
                if marijuana.lower() in lifestyleDescription:
                    lifestylePass = True
                    break

        # check pets/kids (if applicable)
        familyPass = False
        value = waitForSection(driver, 0, False, 'family')
        if value:
            familyDescription = str(driver.find_element_by_class_name('matchprofile-details-section.matchprofile-details-section--family').text).lower()
            for pets in options['Pets']:
                if pets.lower() in familyDescription:
                    familyPass = True
                    break
            for kids in options['Kids']:
                if kids.lower() in familyDescription:
                    familyPass = True
                    break

        # check for intro
        intro = False
        try:
            driver.find_element_by_id('firstmessage2017')
            intro = True
        except:
            pass

        name = driver.find_element_by_class_name("cardsummary-item.cardsummary-realname").text
        profileLink = driver.find_element_by_class_name('cardsummary-item.cardsummary-profile-link')
        link = str(profileLink.get_attribute('innerHTML'))
        link = "https://www.okcupid.com" + link[link.index('href="') + 6:link.index('>', link.index('href="')) - 1]
        if options['Check Intro'].get() and intro:
            swipeList.append([name, matchPercentage, imageCount, wordCount, 'NA', link])
            # swipe right if criteria check is on, left if not
            rightSwipeCount += 1
            if options['Check Criteria'].get():
                cardDeckRightSwipe(driver)
            else:
                cardDeckLeftSwipe(driver)
                leftSwipeCount += 1
        # check qualitative options
        elif phrasePass or basicsPass or bodyTypePass or backgroundPass or lifestylePass or familyPass:
            cardDeckLeftSwipe(driver)
            leftSwipeCount += 1
        # check quantitative options
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
            # make decision if questions check is disabled
            if not options['Check Questions'].get():
                swipeList.append([name, matchPercentage, imageCount, wordCount, 'NA', link])
                # swipe right if criteria check is on, left if not
                rightSwipeCount += 1
                if options['Check Criteria'].get():
                    cardDeckRightSwipe(driver)
                else:
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
                    swipeList.append([name, matchPercentage, imageCount, wordCount, questionCount, link])
                    rightSwipeCount += 1
                    if options['Check Criteria'].get():
                        profileRightSwipe(driver)
                    else:
                        profileLeftSwipe(driver)
                        leftSwipeCount += 1
                else:
                    profileLeftSwipe(driver)
                    leftSwipeCount+=1
        totalSwipeCount+=1
        # update results display
        updateResultsDisplay(options, titleLabel, leftLabel, rightLabel, totalSwipeCount, leftSwipeCount, rightSwipeCount)
        resultsDisplay.update()
        inspectProfileFunction(root, driver, options, resultsDisplay, titleLabel, leftLabel, rightLabel, totalSwipeCount, rightSwipeCount, leftSwipeCount, swipeList, buttons)