#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:52:45 2019

@author: xiaolu
"""

#1. Combine all female and male files from discussion board into 2 files with a Python script.
import os 
from textblob import TextBlob 

def Combine():
    female = []
    male = []
    for file in os.listdir(r'/Users/xiaolu/Desktop/data'):
        if file.startswith('female'):
            with open(file,'r') as f:
                female.extend([(item) for item in (f)])
        if file.startswith('male'):
            with open(file, 'r') as f:
                male.extend([(item) for item in (f)])
    return female, male              


### Clean the text, split the text with a or an, to form a format 
def gettext(x):
    cleanlist = []
    for item in x:
        if 'a' in item:
            y = item.split('a')[1:]
            z = ''
            for i in y:
                z += 'a'+i
        elif 'an' in item:
            y = item.split('an')[-1]
            z = ''
            for i in y:
                z += 'an'+i
        cleanlist.append(z)
    return cleanlist

# 2. Sort all of the characters based on sentiment. Submit top 10 male, top 10 female, bottom 10 male, bottom 10 female
def Bestworst(female, male):
    sentimale = []
    sentifemale = []
# Calculate sentiment for each items
    for i,item in enumerate(female):
        sentifemale.append(TextBlob(item).sentiment[0])
    for i,item in enumerate(female):
        sentimale.append(TextBlob(item).sentiment[0])
# Find out the best and worst items
    bestfe10index = sorted(range(len(sentifemale)), key=lambda i: sentifemale[i])[-10:]
    worstfe10index = sorted(range(len(sentifemale)), key=lambda i: sentifemale[i])[0 : 9]
    bestma10index = sorted(range(len(sentimale)), key=lambda i: sentimale[i])[-10:]
    worstma10index = sorted(range(len(sentimale)), key=lambda i: sentimale[i])[0:9]
    
    bestfemale10 = ["She's " + female[i].replace('\n','') for i in bestfe10index]
    worstfemale10 = ["She's " +female[i].replace('\n','') for i in worstfe10index]
    bestmale10 = ["He's " + male[i].replace('\n','') for i in bestma10index]
    worstmale10 = ["He's "+ male[i].replace('\n','') for i in worstma10index]

# Return the results
    return (bestfemale10, worstfemale10, bestmale10, worstmale10)



# 3. finds the 10 most common descriptions for characters
from collections import Counter
def mostcommon1(female, male):
# Merge all the descriptions together
    description = []
    for i,item in enumerate(female):
        description.extend(item.split(' ')[1:3])
    for i,item in enumerate(male):
        description.extend(item.split(' ')[1:3])
# Count the most common 10 descriptions
    C = Counter(description)
# Return the results
    return [word for word,cnt in C.most_common(10)]


fem, mal = Combine()
f = gettext(fem)
m = gettext(mal)
Bestworst(f, m)
mostcommon1(f, m)




