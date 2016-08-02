import unittest
from appium import webdriver
import xmlrunner
import Buttons
import Fields
import argparse
import sys
import os
from time import sleep
import datetime
import create_wav
import ping_wave


def createParser():
    parser = argparse.ArgumentParser()
    # e7eddca32184875d43aa17f09e268fb4cfe26eec')
    parser.add_argument('-d', '--device_name',
                        default='cc1257db6dd070e229924b58a92bf51e12f93129')
    parser.add_argument('-pl', '--platform', default='iOS')
    parser.add_argument('-l', '--link', default='localhost')
    parser.add_argument('-p', '--port', default='4727')
    parser.add_argument('-f', '--folder', default='iPhone6')
    return parser


def send_message(driver, Phone_number, *Message_text):
    Buttons.TapButtons(driver, 'Keypad', True)
    for digit in Phone_number:
        if digit.isdigit():
            print digit
            Buttons.TapButtons(driver, digit, True)
    Buttons.TapButtons(driver, 'text message', True)
    Message = Fields.GenerateMessage()
    Fields.FindMessageTextField(driver, Message)
    Buttons.TapButtons(driver, 'Send', True)
    Fields.MessageFromYourself(driver, 'in', Message)
    Fields.MessageFromYourself(driver, 'out', Message)
    sleep(1)


def make_a_call(driver, Phone_number):
    Buttons.TapButtons(driver, 'Keypad', True)
    for digit in Phone_number:
        if digit.isdigit():
            print digit
            Buttons.TapButtons(driver, digit, True)
    Buttons.TapButtons(driver, 'make call', True)
    sleep(5)


def prestep(driver):
    Buttons.TapButtons(driver, 'Settings', True)
    Phone_number = driver.find_element_by_xpath(
        '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[2]').text
    Phone_number = str(Phone_number)
    print "My phone nymber: ", Phone_number
    return Phone_number


def keypad_verification(driver, Tapped=False):
    onKeypad = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '#', ' ']
    for button in onKeypad:
        Buttons.TapButtons(driver, button, Tapped)
    Buttons.TapButtons(driver, 'make call', False)  # Always visible
    Buttons.TapButtons(driver, 'text message', False)  # Always visible
    if Tapped == True:
        # visible if some digit was tapping
        Buttons.TapButtons(driver, 'add', False)
        # visible if some digit was tapping
        Buttons.TapButtons(driver, 'erase', False)


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
device_name = namespace.device_name
platform = namespace.platform
port = namespace.port
folder = namespace.folder
link = namespace.link
Phone_number = ''

path_ = os.path.dirname(__file__) + '/' + str(folder) + '/'


class TestAuto(unittest.TestCase):

    def setUp(self):
        parser = createParser()
        namespace = parser.parse_args(sys.argv[1:])
        device_name = namespace.device_name
        platform = namespace.platform
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = platform
        #desired_caps['platformVersion'] = version
        desired_caps['deviceName'] = device_name
        desired_caps['waitForAppScript'] = '$.delay(3500)'
        desired_caps['uuid'] = device_name
        # desired_caps['autoAcceptAlerts']=True
        #desired_caps['launchTimeout'] = '3500'
        # desired_caps['fullReset']=True
        # desired_caps['noReset']=True
        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "set up - OK!"
        sleep(10)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()


    def test_Call_screen(self):
        testname = "Call screen validation"
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        Buttons.TapButtons(self.driver,'Calls',True)
        Buttons.TapButtons(self.driver,'Clear',False)
        Buttons.TapButtons(self.driver,'All',False)
        Buttons.TapButtons(self.driver,'Missed',False)
        Buttons.TapButtons(self.driver,'voicemail', False)
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        print path_
        sleep(10)
'''
    def test_Message_screen(self):
        testname = "Messages screen validation"
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        sleep(5)
        Buttons.TapButtons(self.driver,'Messages',True)
        Buttons.TapButtons(self.driver,'Clear',False)
        Fields.FindStaticField(self.driver, 'Messages')
        Buttons.TapButtons(self.driver,'Compose',False)
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(10)

    def test_Message_screen_Clear_Message_list(self):
        testname = "Clear messages list"
        print "Test start: ",testname
        Phone_number = prestep(self.driver)
        send_message(self.driver,Phone_number)
        Buttons.TapButtons(self.driver,'Keypad',True)
        keypad_verification(self.driver,False)
        Buttons.TapButtons(self.driver,'Messages',True)
        Buttons.TapButtons(self.driver,'Clear', True)
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Confirm Call Deletion"]')
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Are you sure you want to delete these call logs?"]')
        Buttons.TapButtons(self.driver,'Delete', True)
        self.driver.find_element_by_xpath('//UIATableView[@name="Empty list"]')
        self.driver.find_element_by_xpath('//UIAImage[@name="messages_empty"]')
        Clear = self.driver.find_element_by_xpath('//UIAButton[@name="Clear" and @enabled="false"]')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(10)


    def test_Call_screen_Clear_Call_list(self):
        testname = "Call screen  - Clear call list"
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        Phone_number = prestep(self.driver)
        make_a_call(self.driver,Phone_number)
        sleep(3)
        Buttons.TapButtons(self.driver,'Calls',True)
        Buttons.TapButtons(self.driver,'Clear', True)
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Confirm Call Deletion"]')
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Are you sure you want to delete these call logs?"]')
        Buttons.TapButtons(self.driver,'Delete', True)
        self.driver.find_element_by_xpath('//UIATableView[@name="Empty list"]')
        self.driver.find_element_by_xpath('//UIAImage[@name="calls_empty"]')
        Clear = self.driver.find_element_by_xpath('//UIAButton[@name="Clear" and @enabled="false"]')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(10)

    def test_Keypad_screen_Tap_all_keys(self):
        testname = "Keypad screen - Tap all keys "
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        sleep(5)
        Buttons.TapButtons(self.driver,'Keypad',True)
        keypad_verification(self.driver,True) #Tapped all anf find Add and Erase buttons,Call and Message
        Fields.FindStaticField(self.driver, '123456789#*')
        Buttons.TapButtons(self.driver,'erase',True)
        Fields.FindStaticField(self.driver, '123456789#')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(2)



    def test_Setting_screen(self):
        testname = 'Settings screen validation'
        print "Test start: ",testname
        Buttons.TapButtons(self.driver,'Settings',True)
        Fields.FindStaticField(self.driver, 'Credits')
        Fields.FindStaticField(self.driver, 'Talkatone Subscriptions')
        Fields.FindStaticField(self.driver, 'Sounds & Notifications')
        Fields.FindStaticField(self.driver, 'Texting')
        Fields.FindStaticField(self.driver, 'Passcode')
        Fields.FindStaticField(self.driver, 'About Talkatone')

    def test_Message_screen_Clear_Message_list(self):
        testname = "Clear messages list"
        print "Test start: ",testname
        Phone_number = prestep(self.driver)
        send_message(self.driver,Phone_number)
        Buttons.TapButtons(self.driver,'Keypad',True)
        keypad_verification(self.driver,False)
        Buttons.TapButtons(self.driver,'Messages',True)
        Buttons.TapButtons(self.driver,'Clear', True)
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Confirm Call Deletion"]')
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Are you sure you want to delete these call logs?"]')
        Buttons.TapButtons(self.driver,'Delete', True)
        self.driver.find_element_by_xpath('//UIATableView[@name="Empty list"]')
        self.driver.find_element_by_xpath('//UIAImage[@name="messages_empty"]')
        Clear = self.driver.find_element_by_xpath('//UIAButton[@name="Clear" and @enabled="false"]')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(10)



    def test_Message_screen_Clear_Message_list(self):
        testname = "Clear messages list"
        print "Test start: ",testname
        Phone_number = prestep(self.driver)
        send_message(self.driver,Phone_number)
        Buttons.TapButtons(self.driver,'Keypad',True)
        keypad_verification(self.driver,False)
        Buttons.TapButtons(self.driver,'Messages',True)
        Buttons.TapButtons(self.driver,'Clear', True)
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Confirm Call Deletion"]')
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Are you sure you want to delete these call logs?"]')
        Buttons.TapButtons(self.driver,'Delete', True)
        self.driver.find_element_by_xpath('//UIATableView[@name="Empty list"]')
        self.driver.find_element_by_xpath('//UIAImage[@name="messages_empty"]')
        Clear = self.driver.find_element_by_xpath('//UIAButton[@name="Clear" and @enabled="false"]')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(10)


    def test_Setting_screen(self):
        testname = 'Settings screen validation'
        print "Test start: ",testname
        Buttons.TapButtons(self.driver,'Settings',True)
        Fields.FindStaticField(self.driver, 'Credits')
        Fields.FindStaticField(self.driver, 'Talkatone Subscriptions')
        Fields.FindStaticField(self.driver, 'Sounds & Notifications')
        Fields.FindStaticField(self.driver, 'Texting')
        Fields.FindStaticField(self.driver, 'Passcode')
        Fields.FindStaticField(self.driver, 'About Talkatone')

    def test_Call_screen_Clear_Call_list(self):
        testname = "Call screen  - Clear call list"
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        Phone_number = prestep(self.driver)
        make_a_call(self.driver,Phone_number)
        sleep(3)
        Buttons.TapButtons(self.driver,'Calls',True)
        Buttons.TapButtons(self.driver,'Clear', True)
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Confirm Call Deletion"]')
        #self.driver.find_element_by_xpath('//UIAStaticText[@text="Are you sure you want to delete these call logs?"]')
        Buttons.TapButtons(self.driver,'Delete', True)
        self.driver.find_element_by_xpath('//UIATableView[@name="Empty list"]')
        self.driver.find_element_by_xpath('//UIAImage[@name="calls_empty"]')
        Clear = self.driver.find_element_by_xpath('//UIAButton[@name="Clear" and @enabled="false"]')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(10)

    def test_Setting_screen_Sounds(self):
        testname = 'Sounds & Notifications screen validation'
        print "Test start: ",testname
        Buttons.TapButtons(self.driver,'Settings',True)
        Fields.FindStaticField(self.driver, 'Sounds & Notifications',True)
        Fields.FindStaticField(self.driver, 'Sounds & Notifications')
        #Buttons.TapButtons(self.driver,'Settings',False)
        #INCOMING SOUNDS
        INCOMING_SOUNDS = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]')
        print "Fiels \"" + "INCOMING_SOUNDS" +"\" was found. Field text: ", INCOMING_SOUNDS.text
        Fields.FindStaticField(self.driver, 'Vibrate in Foreground')
        Buttons.TapSwitch(self.driver,'Vibrate in Foreground',Tap=False)
        Buttons.TapSwitch(self.driver,'Vibrate in Foreground',Tap=True)
        Fields.FindStaticField(self.driver, 'MessageTone')
        Fields.FindStaticField(self.driver, 'Ring Tone')
        Fields.FindStaticField(self.driver, 'Call Over Tone')
        #-----------------------------------------------
        Fields.FindStaticField(self.driver, 'MessageTone')
        Fields.FindStaticField(self.driver, 'Ring Tone')
        OUTGOING_SOUNDS = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[2]/UIAStaticText[1]')
        print "Fiels \"" + "OUTGOING SOUNDS" +"\" was found. Field text: ", OUTGOING_SOUNDS.text
        OUTGOING_MessageTone = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]/UIAStaticText[1]') # OUTGOING_MessageTone
        print "Fiels \"" + "OUTGOING MessageTone" +"\" was found. Field text: ", OUTGOING_MessageTone.text
        #-----------------------------------------------
        NOTIFICATIONS_PRIVACY = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[3]/UIAStaticText[1]')
        print "Fiels \"" + "NOTIFICATIONS PRIVACY" +"\" was found. Field text: ", NOTIFICATIONS_PRIVACY.text
        Fields.FindStaticField(self.driver, 'Show Summary Only')
        Buttons.TapSwitch(self.driver,'Show Summary Only',Tap=True)
        Buttons.TapSwitch(self.driver,'Show Summary Only',Tap=False)
        PUSH_NOTIFICATIONS = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[4]')
        print "Fiels \"" + "PUSH NOTIFICATIONS" +"\" was found. Field text: ", PUSH_NOTIFICATIONS.text
        Fields.FindStaticField(self.driver, 'Push Notifications')
        Buttons.TapSwitch(self.driver,'Push Notifications',Tap=False)
        Buttons.TapSwitch(self.driver,'Push Notifications',Tap=True)

    def test_Setting_screen_Texting(self):
        testname = 'Texting screen validation'
        print "Test start: ", testname
        Buttons.TapButtons(self.driver, 'Settings', True)
        Fields.FindStaticField(self.driver, 'Texting', True)
        Fields.FindStaticField(self.driver, 'Texting Settings')
        #Buttons.TapButtons(self.driver, 'Settings', False)
        COMPOSING = self.driver.find_element_by_xpath(
            '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableGroup[1]/UIAStaticText[1]')
        print "Fiels \"" + "COMPOSING" + "\" was found. Field text: ", COMPOSING.text
        Fields.FindStaticField(self.driver, 'Autocorrect')
        Buttons.TapSwitch(self.driver,'Autocorrect',Tap=False)
        Buttons.TapSwitch(self.driver,'Autocorrect',Tap=True)
        Fields.FindStaticField(self.driver, 'Picture Edit')
        Buttons.TapSwitch(self.driver,'Picture Edit',Tap=True)
        Buttons.TapSwitch(self.driver,'Picture Edit',Tap=False)
        Fields.FindStaticField(self.driver, 'Save to Camera Roll')
        Buttons.TapSwitch(self.driver,'Save to Camera Roll')
        Buttons.TapSwitch(self.driver,'Save to Camera Roll',Tap=True)
        Buttons.TapSwitch(self.driver,'Save to Camera Roll',Tap=False)
        Fields.FindStaticField(self.driver, 'Signature')

    def test_Setting_screen_About(self):
        testname = 'About screen validation'
        print "Test start: ",testname
        Buttons.TapButtons(self.driver,'Settings',True)
        Fields.FindStaticField(self.driver, 'About Talkatone', True)
        Fields.FindStaticField(self.driver, 'Rate in AppStore')
        Fields.FindStaticField(self.driver, 'Invite Friends')
        Fields.FindStaticField(self.driver, 'FaceBook and Twitter')
        Fields.FindStaticField(self.driver, 'Privacy Policy')
        Fields.FindStaticField(self.driver, 'Terms of Use')
        Fields.FindStaticField(self.driver, 'Legal Notices')


    def test_Contact_screen(self):
        testname = 'Contact screen validation'
        print "Test start: ",testname
        Buttons.TapButtons(self.driver,'Settings',True)
        print 'TBD'

    def test_Keypad_screen(self):
        testname = "Keypad screen validation"
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        sleep(5)
        Buttons.TapButtons(self.driver,'Keypad',True)
        keypad_verification(self.driver,False) #Find digit only, Call and Message
        self.driver.save_screenshot(path_ + str(testname) +'.png')

    def test_Keypad_screen_Tap_all_keys(self):
        testname = "Keypad screen - Tap all keys "
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        sleep(5)
        Buttons.TapButtons(self.driver,'Keypad',True)
        keypad_verification(self.driver,True) #Tapped all anf find Add and Erase buttons,Call and Message
        Fields.FindStaticField(self.driver, '123456789#*')
        Buttons.TapButtons(self.driver,'erase',True)
        Fields.FindStaticField(self.driver, '123456789#')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(2)


    def test_Keypad_screen_Tap_all_keys(self):
        testname = "Keypad screen - Tap all keys "
        print "Test start: ",testname
        Buttons.AreMainButtonsPrersents(self.driver)
        sleep(2)
        Buttons.TapButtons(self.driver,'Keypad',True)
        keypad_verification(self.driver,True) #Tapped all anf find Add and Erase buttons,Call and Message
        sleep(2)
        Fields.FindStaticField(self.driver, '1234567890#*')
        Buttons.TapButtons(self.driver,'erase',True)
        Fields.FindStaticField(self.driver, '1234567890#')
        self.driver.save_screenshot(path_ + str(testname) +'.png')
        sleep(2)


    def test_Setting_screen_Passcode(self):
        testname = 'Passcode screen validation'
        print "Test start: ",testname
        Buttons.TapButtons(self.driver,'Settings',True)
        Fields.FindStaticField(self.driver, 'Passcode',True)
        Fields.FindStaticField(self.driver, 'Passcode')
        Buttons.TapButtons(self.driver,'Settings',False)
        TurnPasscodeOn=self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
        print "Fiels \"" + "COMPOSING" +"\" was found. Field text: ", TurnPasscodeOn.text
        #Switch

    def test_Setting_screen_Passcode_TurnPasscodeOn(self):
        testname = 'TurnPasscodeOn screen validation'
        print "Test start: ",testname
        Buttons.TapButtons(self.driver,'Settings',True)
        Fields.FindStaticField(self.driver, 'Passcode',True)
        Fields.FindStaticField(self.driver, 'Passcode')
        Buttons.TapButtons(self.driver,'Settings',False)
        TurnPasscodeOn=self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]')
        print "Fiels \"" + "COMPOSING" +"\" was found. Field text: ", TurnPasscodeOn.text
        TurnPasscodeOn.click()
        Fields.FindStaticField(self.driver, 'Enter the passcode')
        buttons = ['1','2','3','4','5','6','7','8','9','0','Delete']
        Buttons.iOSKeypadValidation(self.driver,buttons)

    def test_PlayVoicemail(self):
        print "Test start"
        sleep(1)
        self.driver.find_element_by_name('Calls').click()
        self.driver.find_element_by_name('voicemail').click()
        sleep(5)
        self.driver.find_element_by_name('play').click()
        print ("Full Voicemail")
        create_wav.BigEar(os.path.dirname(__file__)+'/'+str(folder)  +'/' + 'Played Voicemail for test')
        sleep(5)
        print("OK!")
        self.driver.find_element_by_name('Calls').click()
        sleep(2)
        self.driver.find_element_by_name('voicemail').click()
        sleep(5)
        self.driver.find_element_by_name('play').click()
        sleep(2)
        self.driver.find_element_by_name('Calls').click()
        create_wav.LittleEar(os.path.dirname(__file__)+'/'+str(folder)  +'/' + 'Empty Voicemail for test')
        ping_wave.count_channel(os.path.dirname(__file__)+'/'+str(folder)  +'/' + 'Played Voicemail for test.wav')
        ping_wave.count_channel(os.path.dirname(__file__)+'/'+str(folder)  +'/' + 'Empty Voicemail for test.wav')

    def test_Tap_SignUp(self):
        print "Test start"
        sleep(1)
        SignUp = self.driver.find_element_by_name('Sign Up')
        SignUp.click()
        print "Tap Sign Up"
        self.driver.save_screenshot(os.path.dirname(__file__)+'/'+str(folder)  +'/sing UP ' + str(datetime.datetime.now())+'.png')
        sleep(10)
        #alert = self.driver.switch_to_alert()
        self.driver.find_element_by_name('OK').click()
        sleep(10)

    def test_Tap_SignIn(self):
        print "Test start"
        sleep(10)
        SignUp = self.driver.find_element_by_name('Sign In')
        SignUp.click()
        print "Tap Sign In"
        self.driver.save_screenshot(os.path.dirname(__file__)+'/'+str(folder)  +'/sing In ' + str(datetime.datetime.now())+'.png')
        sleep(10)
'''


if __name__ == '__main__':
    print "START!"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    # unittest.TextTestRunner().run(suite)
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' ))
    #outfile_ = open("/Users/galaninaa/test-reports/"+ str(folder)+'/' + 'report '+ str(datetime.datetime.now()) + '.xml', "w")
    # os.path.dirname(__file__)+'/'+str(folder) + '/' + 'report' +
    # str(datetime.datetime.now().date()))
    runner = xmlrunner.XMLTestRunner(output=path_)
    # outfile="/Users/galaninaa/test-reports/"+ str(folder))
    runner. run(suite)
    # print "RUN SUITE"
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' ))

    # TAP runner
    #tests_dir = os.path.dirname(os.path.abspath(__file__))
    # loader = unittest.TestLoader() #.loadTestsFromTestCase(ChessAndroidTests)
    #tests = loader.loadTestsFromTestCase(TestAuto)
   # discover(tests_dir)
    #runner = TAPTestRunner()
    # runner.set_outdir('testout')
    #runner.set_format('Hi: {method_name} - {short_description}')
    # runner.run(tests)