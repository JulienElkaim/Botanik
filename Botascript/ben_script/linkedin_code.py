# -*- coding: utf-8 -*-
"""
Code bot Linkedin
"""

# =============================================================================
# IMPORTING
# =============================================================================

from time import sleep
from selenium import webdriver

SCROLL_PAUSE_TIME = 0.5
LOOPS = 3
N_SCROLL = 2

# =============================================================================
# Initialisation
# =============================================================================

class Linkedin:
    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    # pylint: disable= W0702
    # Noexception type value: resolution impossible
    """
    Class to control the bot
    form of arguments:
        - login: mail.
        - pwd: pwd.
        - arg: {
                "number" : 15,
                "name": ["str","ings"],
                "job": ["policeman", "farmer"],
                "places": ["city", "country"],
                "firms": ["Google", "Amazon"],
                "qualifications": ["internship","Degree","Senior"],
                "common_friends": ["MIN"/"MAX", int]
                }

    """
    def __init__(self, login, password, arg):
        """Init variables"""
        self.driver = webdriver.Firefox()
        self.mail = login
        self.password = password
        self.arg = arg
        self.but = "//*[contains(@class, 'js-discover-person-card__action-btn full-width artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view')]"
        #print(self.but, "\n" + str(self.but0), "\nEgalité:", self.but == self.but0)
        self.test = 0
        self.count = 0
        self.connecter = True
        self.connection = True

        print("Argument(s) recieved:", self.arg)

        self.log_to_send = []

# =============================================================================
# Fonctions for others
# =============================================================================

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
            print("Failed to select connection button")

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

    def arg_number(self):
        """
        Not sure the function is functional but try to use argument
        "until" if it is defined
        """
        try:
            if self.count > self.arg["until"]:
                self.test = LOOPS
        except KeyError as error:
            print("KeyError: arg['until'] missing\nError:", error)

    def try_non_existing_arg(self):
        """
        Successful test to show what happend if an argument isn't defined
        """
        try:
            if self.count > self.arg["inexistant"]:
                self.test = LOOPS
        except KeyError as error:
            print("KeyError:", error, "is missing")

# =============================================================================
# Functions for the mains
# =============================================================================

    def login(self):
        """
        Try to login to a web site, Linkedin by default.
        """
        try:
            self.driver.get("https://www.linkedin.com/login")

            self.driver.find_element_by_id("username").send_keys(self.mail)
            self.driver.find_element_by_id("password").send_keys(self.password)
            self.driver.find_element_by_xpath("//button[@type='submit']").submit()
        except:
            self.printer("ERROR:: Unable to connect with this login")

    def page(self):
        """Try to connect to the network page"""
        while self.connection:
            try:
                self.driver.find_element_by_id("mynetwork-nav-item").click()
                self.connection = False
            except:
                sleep(0.5)

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
                if self.test > LOOPS:
                    break

                self.find_connecter()
                self.clickeur()
                self.arg_number()

            self.driver.refresh()

        self.printer("SUCCESS:: Number of connection(s) added: " + str(self.count))

    def close(self):
        """Close the driver"""
        self.driver.close()

    def printer(self, message):
        """
        Send message to a table serving to send logs after.
        """
        self.log_to_send.append(message)

# =============================================================================
# TAG FUNCTION => MAIN
# =============================================================================

    def add(self):
        """
        Used for order.tag == ADD:
            - arg{name, number, job, common_friends}
        """
        self.login()
        self.page()
        self.clicker()
        self.close()

    def post(self):
        """
        Used for order.tag == POST:
            - arg{to set later}
        """
        self.printer("SUCCESS:: TO DO NO POST")

    def postuler(self):
        """
        Used for order.tag == POST:
            - arg{to set later}
        """
        self.printer("SUCCESS:: TO DO NOT POSTULER")


if __name__ == "__main__":
    SESSION = Linkedin("benjamin.soulan@orange.fr", "InCre3dilB356matdES34A", {"until": 5})
    SESSION.add()
