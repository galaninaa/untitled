import sys
import os
from time import sleep
#------------------IPad TabBar Buttons-------------
Ipad_TabBar_Contacts = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[2]', 'Contacts']
Ipad_TabBar_Calls = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[3]', 'Calls']
Ipad_TabBar_Messages = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[4]', 'Messages']
Ipad_TabBar_Voicemail = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[5]', 'Voicemail']
Ipad_TabBar_Keypad = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[6]', 'Keypad']
Ipad_TabBar_Settings = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[7]', 'Settings']
#------------------Keypad Buttons------------------
Ipad_Keypad_1 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[10]', '1']
Ipad_Keypad_2 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[11]', '2']
Ipad_Keypad_3 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[12]', '3']
Ipad_Keypad_4 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[13]', '4']
Ipad_Keypad_5 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[14]', '5']
Ipad_Keypad_6 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[15]', '6']
Ipad_Keypad_7 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[16]', '7']
Ipad_Keypad_8 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[17]', '8']
Ipad_Keypad_9 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[18]', '9']
Ipad_Keypad_0 = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[20]', '0']
Ipad_Keypad_HESH = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[21]', '#']
Ipad_Keypad_STAR = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[19]']
Ipad_Keapad_MakeACall = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[23]', 'make call']
Ipad_Keapad_TextMessage = [
    '//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[23]', 'text message']
Ipad_UseMobileNumber = ['//UIAApplication[1]/UIAWindow[1]/UIAButton[2]']


# ------------------iPhone4------------------
iPhone4_SignIn = ['//UIAApplication[1]/UIAWindow[1]/UIAButton[1]',
                  'Sign In', '//UIAApplication[1]/UIAWindow[1]/UIAButton[3]', 'Sign In']
iPhone4_SignIn_Continue = [
    '//UIAApplication[1]/UIAWindow[1]/UIAButton[2]', 'Continue']
iPhone4_SignIn_Facebook = ['//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]']
iPhone4_SignUp = ['', 'Sign Up']

'''
iPod_tabView ={ 'Contacts': '//UIAButton[@name="Calls" and @visible="true"]',
                'Calls': '//UIAApplication[1]/UIAWindow[1]/UIAButton[4]',
                'Messages': '//UIAApplication[1]/UIAWindow[1]/UIAButton[5]',
                'Keypad': '//UIAApplication[1]/UIAWindow[1]/UIAButton[6]',
                'Settings': '//UIAApplication[1]/UIAWindow[1]/UIAButton[7]',
                '+': ['//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]','plus'],
                'Done': ['//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]','plus']}

'''


# Find and click button by xpath or name
def Click(driver, Button):
    """ All about click"""
    try:
        for i in range(1):
            if driver.find_element_by_xpath(Button[0]) == True:
                Button = driver.find_element_by_xpath(Button[0])
                break
            else:
                if driver.find_element_by_name(Button[1]):
                    Button = driver.find_element_by_xpath(Button[1])
                    break
        print "Button was found:", Button.text
        sleep(1)
        Button.click()
        sleep(1)
        print "Button was tap:", Button.text
    except ValueError:
        print "Error:", sys.exc_info()
        return False


def TapButtons(driver, Name, Tap):
    try:
        Button = driver.find_element_by_xpath(
            '//UIAButton[@name="' + str(Name) + '" and @visible="true"]')
        if Tap == True:
            Button.click()
            print "Button " + str(Name) + " was found and tapped:", Button.text
        else:
            print "Button  " + str(Name) + " was found:", Button.text
    except ValueError:
        print "Error:", sys.exc_info()
        return False


def AreMainButtonsPrersents(driver):
    Buttons = ['Calls', 'Messages', 'Contacts', 'Keypad', 'Settings']
    for button in Buttons:
        TapButtons(driver, button, False)


def iOSKeypadValidation(driver, Name, Tap=False):
    for element in Name:
        Button = driver.find_element_by_xpath(
            '//UIAKey[@name="' + str(element) + '"]')
        if Tap == True:
            Button.click()
            print "Button " + str(Name) + " was found and tapped:", Button.text



def TapSwitch(driver, Name, Tap=None):
    # Find switch on screen
    # If you want find only, please use: Tap = None
    # If you want find and activate switch, please use: Tap = True
    # If you want find and deactivate switch, please use: Tap = False

    try:
        Switch = driver.find_element_by_xpath('//UIASwitch[@name="' + str(Name) +'"]')
        if Tap == True:
            print Switch.get_attribute("value")
            if Switch.get_attribute("value")==0:
                Switch.click()
            print "Switch " + str(Name) + " was found and activated:", Switch.text
        elif Tap==False:
            if Switch.get_attribute("value")==1:
                Switch.click()
            print "Switch " + str(Name) + " was found and deactivated:", Switch.text
        else:
            print "Switch  " + str(Name) + " was found:", Switch.text


    except ValueError:
        print "Error:", sys.exc_info()
        return False