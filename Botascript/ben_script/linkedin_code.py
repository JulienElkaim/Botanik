# -*- coding: utf-8 -*-
"""
Code bot Linkedin
"""

# =============================================================================
# IMPORTING
# =============================================================================

import sys
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
        - password: pwd.
        - arg: {
                "until" : 15,
                "name": ["str","ings"],
                "job": ["policeman", "farmer"],
                "school": ["HEC Paris", "ICN BS"]
                "places": ["city", "country"],
                "current_e": ["Google", "Amazon"],
                "former_e": ["Google", "Amazon"],
                "message" : "long string"
                }

    """
    def __init__(self, login, password, arg):
        """Init variables"""
        self.driver = webdriver.Firefox()
        self.mail = login
        self.password = password
        self.arg = arg

        self.test = 0
#Any try to add is taken in count so even if first one doesn't work it will increment
        self.count = -1
        self.log_to_send = []

        print("Argument(s) recieved:", self.arg)

        self.login()
        self.page()

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

    def mini_scroll(self):
        """Scroll less than scroll function does"""
        # Get scroll height
        self.driver.execute_script("window.scrollBy(0,200)")

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
                sleep(1)
                try:
                    inputs[string].send_keys(Keys.DOWN)
                    inputs[string].send_keys(Keys.ENTER)
                except:
                    self.printer("WARNING:: Failed to enter '" + str(lieu) +
                                 "' : not in Linkedin database.")
                    inputs[string].clear()

    def add_filtered(self, page):
        """
        connect to the result of the page result
        """
        ref = ("search-result__action-button.search-result__actions--primary.a"
               "rtdeco-button.artdeco-button--default.artdeco-button--2.artdec"
               "o-button--secondary")
        for _ in range(5):
            buttons_connection = self.driver.find_elements_by_class_name(ref)
            if buttons_connection:
                for connection in buttons_connection:
                    if connection.is_enabled():
                        try:
                            connection.click()
                            sleep(1)
                            self.driver.find_element_by_class_name("artdeco-but"
                                                                   "ton.artdeco"
                                                                   "-button--3.ml1").click()
                            sleep(1)
                            self.count += 1
                        except:
                            print("Failed to connect")
            else:
                self.printer("WARNING:: No people to connect resulting from th"
                             "e filtering")
            self.mini_scroll()

        url = self.driver.current_url + "&page=" + str(page)
        self.driver.get(url)


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
        if "Security" in self.driver.title:
            self.printer("ERROR:: Linkedin Security check, order aborted")
            sys.exit()
        connect = True
        while connect:
            try:
                self.driver.find_element_by_id("mynetwork-nav-item").click()
                connect = False
            except:
                sleep(0.5)

    def clicker(self):
        """
        Try to click on everyone, reload
        at most LOOPS times before stopping
        """
        selection_issue = False

        while self.test < LOOPS:
            self.scroll()
            sleep(0.5)
            for _ in range(50):
                if self.test > LOOPS:
                    break
                but = ("js-discover-person-card__action-btn.full-width.artdeco-b"
                       "utton.artdeco-button--2.artdeco-button--full.artdeco-but"
                       "ton--secondary.ember-view")
                try:
                    connecter = self.driver.find_element_by_class_name(but)
                except:
                    selection_issue = True
                try:
                    connecter.click()
                    self.count += 1
                except:
                    self.test += 1
                self.until_limit()
            self.driver.refresh()
        if selection_issue:
            self.printer("WARNING:: Some connection button, where disabled")

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
            - until: int.
            - relation: personnes en relation à une autre
            - lieux[]
            - current_e[]: entreprise actuelle
            - former_e[]: entreprise précédente
            - sector[]
            - school[]


        C'est complètement une très mauvaise idée de faire par requete http.
        """

        self.driver.get('https://www.linkedin.com/search/results/people/?facet'
                        'Network=["S"]')
        self.driver.find_element_by_class_name(("search-filters-bar__all-filter"
                                                "s.flex-shrink-zero.mr3.artdeco"
                                                "-button.artdeco-button--muted."
                                                "artdeco-button--2.artdeco-butt"
                                                "on--tertiary.ember-view")).click() #filtre

        form = []
        form.append(self.driver.find_element_by_xpath("/html/body/div[3]/artde"
                                                      "co-modal-overlay/artdec"
                                                      "o-modal/artdeco-modal-c"
                                                      "ontent/div/div[1]/ul/li"
                                                      "[2]/form/div/fieldset/o"
                                                      "l/li/div/div/input"))
        form.append(self.driver.find_element_by_xpath("/html/body/div[3]/artde"
                                                      "co-modal-overlay/artdec"
                                                      "o-modal/artdeco-modal-c"
                                                      "ontent/div/div[1]/ul/li"
                                                      "[3]/form/div/fieldset/o"
                                                      "l/li[1]/div/div/input"))
        form.append(self.driver.find_element_by_xpath("/html/body/div[3]/artde"
                                                      "co-modal-overlay/artdec"
                                                      "o-modal/artdeco-modal-c"
                                                      "ontent/div/div[1]/ul/li"
                                                      "[4]/form/div/fieldset/o"
                                                      "l/li[1]/div/div/input"))
        form.append(self.driver.find_element_by_xpath("/html/body/div[3]/artde"
                                                      "co-modal-overlay/artdec"
                                                      "o-modal/artdeco-modal-c"
                                                      "ontent/div/div[1]/ul/li"
                                                      "[5]/form/div/fieldset/o"
                                                      "l/li[1]/div/div/input"))
        form.append(self.driver.find_element_by_xpath("/html/body/div[3]/artde"
                                                      "co-modal-overlay/artdec"
                                                      "o-modal/artdeco-modal-c"
                                                      "ontent/div/div[1]/ul/li"
                                                      "[6]/form/div/fieldset/o"
                                                      "l/li[1]/div/div/input"))
        form.append(self.driver.find_element_by_xpath("/html/body/div[3]/artde"
                                                      "co-modal-overlay/artdec"
                                                      "o-modal/artdeco-modal-c"
                                                      "ontent/div/div[1]/ul/li"
                                                      "[8]/form/div/fieldset/o"
                                                      "l/li[1]/div/div/input"))

        inputs = {"relation": form[0], "lieux": form[1],
                  "current_e": form[2], "former_e": form[3],
                  "sector": form[4], "school": form[5]}

        for string in inputs:
            self.formulaire(inputs, string)

        ref = ("search-advanced-facets__button--apply.ml4.mr2.artdeco-button.a"
               "rtdeco-button--3.artdeco-button--primary.ember-view")
        boutton_filtre = self.driver.find_element_by_class_name(ref)
        boutton_filtre.click()
        sleep(2)

        page = 1
        objectif = 50
        if "until" in self.arg:
            objectif = self.arg["until"]
        for _ in range(int(objectif/10)):
            self.add_filtered(page)
            page += 1

# =============================================================================
# TAG FUNCTION => MAIN
# =============================================================================
    def add(self):
        """
        Used for order.tag == "ADD":
            - arg{until, name, number, job, common_friends}
        """
        if not ((("until" in self.arg) and len(self.arg) == 1)
                or not self.arg): #not arg == True => arg non vide
            self.add_specific()
        else:
            self.clicker()
        self.printer("SUCCESS:: Number of connection(s) added: " + str(self.count))

    def post(self):
        """
        Used for order.tad == POST
            arg{message: "post à mettre"}
        """
        sleep(3)
        self.driver.find_element_by_class_name("share-box__open.share-box__tri"
                                               "gger.p4.hoverable-link-text.t-"
                                               "16.t-black--light.t-bold").click()
        box_to_fill = self.driver.find_element_by_class_name("mentions-textedi"
                                                             "tor__contentedit"
                                                             "able.t-18.t-blac"
                                                             "k--light.t-normal")
        for line in self.arg["message"].split("\n"):
            box_to_fill.send_keys(line)
            box_to_fill.send_keys(Keys.ENTER)
        self.driver.find_element_by_class_name("share-actions__primary-action."
                                               "artdeco-button.artdeco-button-"
                                               "-2.artdeco-button--primary.emb"
                                               "er-view").click()
        self.printer("SUCCESS:: message posted")

    def like(self):
        """
        used for order.tag == "LIKE":
            arg{"keyword":"info", "person":"name forname"}
        """

        if "keyword" not in self.arg:
            self.arg["keyword"] = ""

        url = ('https://www.linkedin.com/search/results/content/?keywords='
               + self.arg["keyword"])
        self.driver.get(url)
        like = self.driver.find_elements_by_class_name("react-button__trigger.a"
                                                       "rtdeco-button.artdeco-b"
                                                       "utton--muted.artdeco-bu"
                                                       "tton--4.artdeco-button-"
                                                       "-tertiary.ember-view")
        for element in like:
            try:
                element.click()
            except:
                print("beug de merde")
            self.scroll()
        self.printer("SUCCESS:: Some likes where made")

    def postuler(self):
        """
        Used for order.tag == "POSTING":
            - arg{to set later}
        """
        self.printer("SUCCESS:: TO DO NOT POSTULER")

# =============================================================================
# if __name__ == "__main__":
#     SESSION = Linkedin("victor.ben-ami@hotmail.com", "Vo0RdQBkNZrB2usB9Hum",
#                        {"until": 5,
# # =============================================================================
# #                         "message":("It real sent your at. Amounted all shy set"
# #                                    "why followed declared. Repeated of endeavo"
# #                                    "r mr position kindness offering ignorant s"
# #                                    "o up. Simplicity are melancholy preference"
# #                                    "considered saw companions. Disposal on out"
# #                                    "weigh do speedily in on. Him ham although "
# #                                    "thoughts entirely drawings. Acceptance unr"
# #                                    "eserved old admiration projection nay yet "
# #                                    "him. Lasted am so before on esteem vanity "
# #                                    "oh.\nFriendship contrasted solicitude insi"
# #                                    "pidity in introduced literature it. He see"
# #                                    "med denote except as oppose do spring my."),
# # =============================================================================
#                         #"lieux": ["France", "Royaume-uni"],
#                         #"current_e":["bn"],
#                         #"former_e":["dior"],
#                         #"keyword":"Artificial Intelligence",
#                         # sector":["banque"],
#                         #"school":["hec paris", "ICN"]
#                        })
# # =============================================================================
# #                        {"until": 5,
# #                         "lieux": ["France", "Royaume-uni"],
# #                         "current_e":["bn"],
# #                         "former_e":["societe ge", "rotschild"],
# #                         "sector":["banque"],
# #                         "school":["hec paris", "ICN"]
# #                        })
# # =============================================================================
#
#
#     SESSION.add()
#     #SESSION.like()
#     #SESSION.post()
#     for info in SESSION.log_to_send:
#         print(info)
# =============================================================================
