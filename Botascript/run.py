h #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:33:59 2019

@author: benjamin et julien

A faire en cas de manque de db dans Botaserver:

- Vérifier que ruby fonctionne avec irb.
- Si non faire : 'bash --login' et 'rvm use 2.4.4
- Initialiser la db:
    'rake db:drop && rake db:create && rake db:migrate && rake db:seed'

ATTENTION A NE PAS METTRE DE ";" DANS LES LOGS
"""

from ben_script.order_treatment import read
from back_process.Interface import getFakeDB
from back_process.Interface import Orders


#===============/!\ IGNORE IT /!\=======================
# =============================================================================
# ordersToExec = Orders() # Orders list creation, empty.
# ordersToExec.getWork() # Fill the list with orders to execute.
# =============================================================================
def crash():
    """Do whatever you want here"""
    getFakeDB() #Erase DB and create fake records.
    orders_to_exec = Orders()
    orders_to_exec.getWork()
    print("=========== THIS IS A WAR ZONE =============")
    counter = 0
    for _ in orders_to_exec:
        counter += 1
        print(counter, ": Everything is fine")
    # Dirty stuff

def dev():
    """Developping side of this file"""
    getFakeDB()
    orders_to_exec = Orders()
    orders_to_exec.getWork()

    print("=========== DEVELOPMENT MODE ===========")

    for order in orders_to_exec:
        read(order)
        break

    orders_to_exec.finished() #Ensure to notify database

def prod():
    """Production side of this file"""
    orders_to_exec = Orders()
    orders_to_exec.getWork()
    print("=========== PRODUCTION ================")

    for _ in orders_to_exec:
        # /!\ Ton code ICI /!\
        pass


    orders_to_exec.finished() #Ensure to notify database

if __name__ == "__main__":

    MODE = {"CRASH": False, "DEV": True, "PROD": False}

    if MODE["CRASH"]:
        crash()
    if MODE["DEV"]:
        dev()
    if MODE["PROD"]:
        prod()
