from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import random
import sys
import time


class InstagramBot:
    #enter login credentials here
    username = 'user'
    password = 'pass'

    #fill in with desired hashtags
    hashtags = []

    #add your comments here
    comments = ['Roar, what a really nice photo :)', 'Roar, your posts are amazing', 'Roar, You are awesome! Never forget that.', 'Roar, Beautiful. Definition: A person who is reading this.', 'Roar, An original is worth more than a copy, so always be yourself!', 'Roar, Life is better when you’re laughing.', 'Roar, thank you for being you!']

    def __init__(self):
        self.browser = webdriver.Safari()
        self.login()
        randomtag = random.choice(self.hashtags)
        self.doGood(randomtag)

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)

        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.send_keys(self.username)
        time.sleep(1)

        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(4)

    def doGood(self, hashtag):
        driver = self.browser
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        pic_hrefs = []
        for i in range(1, 3):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try: 
                self.follow_user()
                time.sleep(2)
                self.comment()
                time.sleep(2)
                self.like()
                time.sleep(2)
            except Exception as e:
                time.sleep(2)

    def comment(self):
        #print("running comment")
        comment_input = lambda: self.browser.find_element_by_tag_name('textarea')
        comment_input().click()
        comment_input().clear()

        comment = random.choice(self.comments)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = random.randint(1, 7) / 30
            time.sleep(delay)

        comment_input().send_keys(Keys.RETURN)
        #print("commented on post")

    def follow_user(self):
        #print('running follow')
        time.sleep(4)
        try:
            time.sleep(4)
            self.browser.find_element_by_xpath("//header//button[text()=\"Follow\"]").click()
            time.sleep(4)
        except Exception as e:
            print("Follow button not found")
        #print('following user')

    def like(self):
        time.sleep(3)
        #print('running like')
        try:
            like_button = self.browser.find_element_by_class_name('fr66n').click()
        except Exception as e:
            print("Rest")
        #print("liked post")

    def finalize(self):
        self.browser.close()
        sys.exit()

instagramBot = InstagramBot()
