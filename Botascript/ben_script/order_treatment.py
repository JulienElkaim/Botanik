#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:33:59 2019

@author: benjamin

DEPENDANCE: imported by run.py and takes object Order.
Principal function is read().
"""

from ben_script.linkedin_code import Linkedin

def start():
    """test to understand how to formulate the code"""
    print("\n=== DEBUT D'UN ORDRE ===")

def read(order):
    """
    Takes Object Order to use it and redirect it to the right function
    """
    start()
    print("login   :", order.login)
    print("password:", order.password)
    print("network :", order.network)
    print("tag     :", order.tag)
    print("args    :", order.args)
    print(order.args.__class__)
    print("log     :", order.log)

# =============================================================================
#     if(order.network == "INSTAGRAM"):
#         Session = Instagram(order.login, order.password, order.network, order.arg)
#     if(order.network == "FACEBOOK"):
#         Session = Facebook(order.login, order.password, order.network, order.arg)
#     else:
# =============================================================================
    session = Linkedin(order.login, order.password, order.args)

# =============================================================================
#     if(order.tag == "ADD"):
#         Session.add()
#     if(order.tag == "POST"):
#         Session.post()
#     if(order.tag == "POSTULER"): #unique for Linkedin
#         Session.postuler
# =============================================================================
    #order.log(Session.log_to_send)
    session.add()
    session.post()
    session.postuler()

    print(session.log_to_send)
