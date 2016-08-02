__author__ = 'galaninaa'
import sys
import random

from time import sleep
#------------------IPad TabBar Buttons-------------
EditContact_FirstName = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]'
EditContact_LastName = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]'
EditContact_AddFirstPhoneNumber = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIATextField[1]'


def AddData(driver,Field,Data):
    Field_ =driver.find_element_by_xpath('//UIATextField[@value="'+str(Field)+'"]')
    if Field_:
        Field_.set_value(Data)
        print "Fiels \"" + Field +"\" was found and added data: ", Data

                

def FindStaticField(driver, Field, Clickable=False):
    try:
        Element =driver.find_element_by_xpath('//UIAStaticText[@name="'+str(Field) + '"]')
        print "Fiels \"" + Field +"\" was found. Field text: ", Element.text
        if Clickable==True:
            Element.click()
            print "Fiels \"" + Field +"\" was clicked. Field text: ", Element.text
    except ValueError:
        print "Fiels \"" + Field +"\" wasn't found"
        print "Error:", sys.exc_info()
        return False


def MessageFromYourself(driver,route,Message):
    if route == 'in':
        try:
            MessageField=driver.find_element_by_xpath('//UIATextView[@value="' + Message +'" and @x<"42"]')
            print "Incoming message: \"" + Message +"\""
        except ValueError:
            print "Incoming message \"" + Message +"\" wasn't found"
            print "Error:", sys.exc_info()
            return False
    if route == 'out':
        try:
            MessageField=driver.find_element_by_xpath('//UIATextView[@value="' + Message +'" and @x>"42"]')
            print "Outgoing message: \"" + Message +"\""
        except ValueError:
            print "Outgoing message \"" + Message +"\" wasn't found"
            print "Error:", sys.exc_info()
            return False


def FindMessageTextField(driver,Message):
    try:
        MessageField = driver.find_element_by_xpath('//UIATextView[@value="" and @name="" and @label=""]')
        MessageField.click()
        sleep(1)
        MessageField.set_value(Message)
        print "Message field was found. Add text: ", Message
    except ValueError:
        print "Message field wasn't found"
        print "Error:", sys.exc_info()
        return False

def GenerateMessage():
    start = ['Hello!','Hi!','Maaaan!','Dude!','Halo!','Good morning!','How\'s it going?','Howdy!','Hiya!','Yo!','Nice to see you.','What\'s new?']
    middle = ['WTSP??', 'How are you?','Are you drunk?','Bad idia.','Good news!','Are you here?','Can I offer you something to drink?','The food looks great. I can\'t wait to try the dessert.','Please, call me BOSS!']
    middle2 = ['My mum is not home', 'Let\' drink?','Meeting?','Kiss me?','I wath TV.', 'Sasha Greay is the BEST!!','Have we met before?','Can you say it again, please? ','No problem.','You\'ve got to be kidding me! ']
    end = ['That all!', 'Sleeep...',':)','OMG...','Mmm???','I\'d better be going','See you later! See you around! ']
    return random.choice(start)+random.choice(middle)+random.choice(middle2) + random.choice(end)


__author__ = 'galaninaa'
import sys
import random

from time import sleep
#------------------IPad TabBar Buttons-------------
EditContact_FirstName = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[1]'
EditContact_LastName = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[1]/UIATableCell[2]'
EditContact_AddFirstPhoneNumber = '//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATableView[2]/UIATableCell[1]/UIATextField[1]'


def AddData(driver,Field,Data):
    Field_ =driver.find_element_by_xpath('//UIATextField[@value="'+str(Field)+'"]')
    if Field_:
        Field_.set_value(Data)
        print "Fiels \"" + Field +"\" was found and added data: ", Data



def FindStaticField(driver, Field, Clickable=False):
    try:
        Element =driver.find_element_by_xpath('//UIAStaticText[@name="'+str(Field) + '"]')
        print "Fiels \"" + Field +"\" was found. Field text: ", Element.text
        if Clickable==True:
            Element.click()
            print "Fiels \"" + Field +"\" was clicked. Field text: ", Element.text
    except ValueError:
        print "Fiels \"" + Field +"\" wasn't found"
        print "Error:", sys.exc_info()
        return False


def MessageFromYourself(driver,route,Message):
    if route == 'in':
        try:
            MessageField=driver.find_element_by_xpath('//UIATextView[@value="' + Message +'" and @x<"42"]')
            print "Incoming message: \"" + Message +"\""
        except ValueError:
            print "Incoming message \"" + Message +"\" wasn't found"
            print "Error:", sys.exc_info()
            return False
    if route == 'out':
        try:
            MessageField=driver.find_element_by_xpath('//UIATextView[@value="' + Message +'" and @x>"42"]')
            print "Outgoing message: \"" + Message +"\""
        except ValueError:
            print "Outgoing message \"" + Message +"\" wasn't found"
            print "Error:", sys.exc_info()
            return False


def FindMessageTextField(driver,Message):
    try:
        MessageField = driver.find_element_by_xpath('//UIATextView[@value="" and @name="" and @label=""]')
        MessageField.click()
        sleep(1)
        MessageField.set_value(Message)
        print "Message field was found. Add text: ", Message
    except ValueError:
        print "Message field wasn't found"
        print "Error:", sys.exc_info()
        return False

def GenerateMessage():
    start = ['Hello!','Hi!','Maaaan!','Dude!','Halo!','Good morning!','How\'s it going?','Howdy!','Hiya!','Yo!','Nice to see you.','What\'s new?']
    middle = ['WTSP??', 'How are you?','Are you drunk?','Bad idia.','Good news!','Are you here?','Can I offer you something to drink?','The food looks great. I can\'t wait to try the dessert.','Please, call me BOSS!']
    middle2 = ['My mum is not home', 'Let\' drink?','Meeting?','Kiss me?','I wath TV.', 'Sasha Greay is the BEST!!','Have we met before?','Can you say it again, please? ','No problem.','You\'ve got to be kidding me! ']
    end = ['That all!', 'Sleeep...',':)','OMG...','Mmm???','I\'d better be going','See you later! See you around! ']
    return random.choice(start)+random.choice(middle)+random.choice(middle2) + random.choice(end)


