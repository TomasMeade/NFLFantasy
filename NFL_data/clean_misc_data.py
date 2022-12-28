#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:33:44 2022

@author: tomasmeade
"""
import pickle

with open('misc_df_dic.pickle', 'rb') as handle:
    misc_df_dic = pickle.load(handle)
    
keys = list(misc_df_dic.keys())


import re

mylist = ["dog", "cat", "wildcat", "thundercat", "cow", "hooo"]
r = re.compile(".*cat")
newlist = list(filter(r.match, mylist)) # Read Note below