#!/usr/bin/python
# -*- coding: utf-8 -*-

import time; #time module
import os, sys

userCommand = 0
commandDir = {'h': 'help', 'help': 'help', 'mkf': 'make folder'}

def createFolderName():
    year1 = time.asctime(time.localtime(time.time()) )
    strLen = len(year1)
    strLen2 = strLen-4
    year1 = year1[strLen2:strLen]
    year1 = str(year1)
    year2 = int(year1[2:4])
    year2 = year2+1
    year2 = str(year2)
    folderName = year1 +  "-" + year2
    return folderName

def assignClassAndSection(studyClass, section, group):
    classCode = {'1':'i', '2':'ii', '3': 'iii', '4': 'iv', '5': 'v', '6': 'vi', '7': 'vii', '8': 'viii', '9': 'ix', '10': 'x', '11': 'xi', '12':'xii'}
    groupFolder = classCode[studyClass] + str(section) +  group
    return groupFolder

def accessFolder(password):
    correct = 0
    if correct:
        print "Access Granted"
        showFolder()
    else:
        print "Access Denied"

def createFolder(groupFolderName):
    path = '/Users/nirmalya/Desktop/folders/' + groupFolderName
    if not os.path.exists(path):
        os.mkdir(path, 0755)
    else:
        print "Folder already exists!"


def takeCommand():
    userCommand = raw_input("enter command>> ")
    userCommand = str(userCommand)
    commandSelected = commandDir[userCommand]
    return commandSelected;

# Program starts here

print "Welcome to File Management (FileMan)"
print "type h/help for help"

studyClass = raw_input("Class: ")
section = raw_input("Section: ")
group = raw_input("Group: ")
groupFolderName = assignClassAndSection(studyClass, section, group)
createFolder(groupFolderName)
