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
                        default='e7eddca32184875d43aa17f09e268fb4cfe26eec')
    parser.add_argument('-pl', '--platform', default='iOS')
    parser.add_argument('-l', '--link', default='localhost')
    parser.add_argument('-p', '--port', default='4727')
    parser.add_argument('-f', '--folder', default='ipod')
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
        desired_caps['waitForAppScript'] = '$.delay(35000)'
        desired_caps['uuid'] = device_name
        # desired_caps['autoAcceptAlerts']=True
        desired_caps['launchTimeout'] = '350000'
        # desired_caps['fullReset']=True
        # desired_caps['noReset']=True
        self.driver = webdriver.Remote(
            'http://' + str(link) + ':' + str(port) + '/wd/hub', desired_caps)
        print "set up - OK!"
        sleep(10)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()


    def test_CallFromiPodToiPhone(self):
        print 'Test start:'
        Call = self.driver.find_element_by_xpath(' //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]')
        Call.click()
        print "Call started"
        sleep(10)
        hang_up = self.driver.find_element_by_name('decline')
        print "I see hang Up. I will sleep 30 seconds"
        sleep(200)
        print 'Test passed'
        sleep(5)



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