# -*- coding: utf-8 -*-
"""
Code bot Linkedin
"""

# =============================================================================
# IMPORTING
# =============================================================================

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
                "until" : 15,
                "name": ["str","ings"],
                "job": ["policeman", "farmer"],
                "school": ["HEC Paris", "ICN BS"]
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

    def until_limit(self):
        """
        Not sure the function is functional but try to use argument
        "until" if it is defined
        """
        if "until" in self.arg:
            if self.count >= self.arg["until"]:
                self.test = LOOPS + 1

    def try_non_existing_arg(self):
        """ Successful test to show what happend if an argument isn't defined"""
        try:
            if self.count > self.arg["inexistant"]:
                self.test = LOOPS
        except KeyError as error:
            print("KeyError:", error, "is missing")

    def formulaire(self, inputs, string):
        """ Fill formulaires to filter the research"""
        if string in self.arg:
            for lieu in self.arg[string]:
                inputs[string].clear()
                inputs[string].send_keys(lieu)
                sleep(2)
                try:
                    inputs[string].send_keys(Keys.ENTER)
                except:
                    self.printer("WARNING:: Failed to enter '" + str(lieu) +
                                 "' : not in Linkedin database.")
                    inputs[string].clear()


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
                self.until_limit()

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
# TEST
# =============================================================================
    def add_specific(self):
        """
        'Override' of add function to connect with specific people

        connexion à l'adresse "https://www.linkedin.com/search/results/people/?facetNetwork=["S"]"

        forme des arguments php:
            (- 2e relation: &facetNetwork=["S"])
            - mot clé (très aléatoire): &keywords=string
            - école: &school=string
            - page: &page=int
            - entreprise actuelle: &facetCurrentCompany=["int", "int"]

        forme des arguments à créer, les chaînes de caractères à gérer doivent
        être précises:
            - relation: personnes en relation à une autre
            - lieux[]
            - current_e[]: entreprise actuelle
            - former_e[]: entreprise précédente
            - sector[]
            - school[]


        C'est complètement une très mauvaise idée de faire par requete http.
        """

        self.driver.get('https://www.linkedin.com/search/results/people/?facetNetwork=["S"]')
        self.driver.find_element_by_class_name("search-filters-bar__all-filters.flex-shrink-zero.mr3.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--tertiary.ember-view").click() #filtre
        formulaire = self.driver.find_elements_by_class_name("ember-text-field.ember-view")
        inputs = {"relation": formulaire[0], "lieux": formulaire[1],
                  "current_e": formulaire[2], "former_e": formulaire[3],
                  "sector": formulaire[4], "school": formulaire[5]}

        for string in inputs:
            self.formulaire(inputs, string)
        boutton_appliquer_filtre = self.driver.find_element_by_class_name("search-advanced-facets__button--apply.ml4.mr2.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
        boutton_appliquer_filtre.click()

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
        if not ((("until" in self.arg) and len(self.arg) == 1)
                or not self.arg): #not arg == True => arg non vide
            self.add_specific()
        else:
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
    SESSION = Linkedin("benjamin.soulan@orange.fr", "InCre3dilB356matdES34A",
                       {"until": 5})
# =============================================================================
#                         ,
#                         "lieux": ["France", "Royaume-uni"],
#                         "current_e":["bn"],
#                         "former_e":["societe ge", "rotschild"],
#                         "sector":["banque"],
#                         "school":["hec paris", "ICN"]
# =============================================================================

    SESSION.add()
    for info in SESSION.log_to_send:
        print(info)
