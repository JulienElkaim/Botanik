#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:33:59 2019

@author: benjamin

DEPENDANCE: imported by run.py and takes object Order.
Principal function is read().
"""

#import linkedin_code to use later

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
    print("log:", order.log)
    print("network:", order.network)
    print("args:", order.args)
    print("tag:", order.tag)
