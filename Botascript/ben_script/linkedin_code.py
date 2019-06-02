# -*- coding: utf-8 -*-
"""
Code bot Linkedin
"""
#import logging

from time import sleep
from datetime import datetime
from selenium import webdriver
#from time import time
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#logger = logging.getLogger()

SCROLL_PAUSE_TIME = 0.5
LOOPS = 3
N_SCROLL = 2


class Fire:
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    # pylint: disable= W0702
    # Noexception type value: resolution impossible
    """Class to control the bot"""
    def __init__(self, login, password):
        """Init variables"""
        self.driver = webdriver.Firefox()
        self.test = 0
        self.count = 0
        self.connecter = True
        self.connection = True
        self.mail = login
        self.password = password
        self.but = "//*[contains(@class, 'js-discover-person-card__action-btn full-width artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view')]"
        #print(self.but, "\n" + str(self.but0), "\nEgalité:", self.but == self.but0)

    def login(self):
        """Try to log in to the web site"""
        try:
            self.driver.get("https://www.linkedin.com/login")

            self.driver.find_element_by_id("username").send_keys(self.mail)
            self.driver.find_element_by_id("password").send_keys(self.password)
            self.driver.find_element_by_xpath("//button[@type='submit']").submit()
        except:
            self.printer("Erreur de login")

    def page(self):
        """Try to connect to the network page"""
        while self.connection:
            try:
                self.driver.find_element_by_id("mynetwork-nav-item").click()
                self.connection = False
            except:
                sleep(0.5)

    def scroll(self):
        """Scroll N_SCROLL times"""
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        for _ in range(N_SCROLL):
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def find_connecter(self):
        """Set driver ready to click on 'se connecter' button"""
        try:
            self.connecter = self.driver.find_element_by_xpath(self.but)
        except:
            #logger.error("Fail to select connection button: " + str(e))
            self.printer("Failed to select connection button")

    def clickeur(self):
        """Count successful connection(s) or refresh page"""
        try:
            self.connecter.click()
            #print(self.count, "Everything is fine")
            self.count += 1
        except:
            #logger.error("Failed to click: " + str(e))
            #print("Failed to click")
            self.test += 1

    def clicker(self):
        """
        Try to click on everyone, reload
        at most LOOPS times before stopping
        """
        self.count -= 1
        while(self.connecter and self.test < LOOPS):
            self.scroll()
            sleep(0.5)
            for _ in range(50):
                self.find_connecter()
                self.clickeur()
                if self.test > LOOPS:
                    break
            self.driver.refresh()

        self.printer("Number of connection(s) added: " + str(self.count))
# =============================================================================
#         print("\nEnd of the session due to more than ", LOOPS, " refresh.\n"
#               "Number of connection(s) added: ", self.count, "\n")
# =============================================================================
    def close(self):
        """Close the driver"""
        self.driver.close()

    def printer(self, message):
        """Print date with message automatically"""
        now = datetime.now()
        print("[" + now.strftime("%Y-%m-%d %H:%M:%S") + "]",
              str(self.mail) + ":", message)

if __name__ == "__main__":
    #start = time()

    SESSION = Fire("nim", "portequoi")
    #fire = str(time() - start)[0:3]

    SESSION.login()
    #login = str(time() - start)[0:3]

    SESSION.page()
    #page = str(time() - start)[0:3]

    SESSION.clicker()
    #clicker = str(time() - start)[0:3]

    SESSION.close()
    #end = str(time() - start)[0:3]

# =============================================================================
#     print("execution time fire =", fire + "s")
#     print("execution time login =", login + "s")
#     print("execution time page =", page + "s")
#     print("execution time clicker =", clicker + "s")
#     print("TOTAL EXECUTION TIME =", end + "s")
# =============================================================================
