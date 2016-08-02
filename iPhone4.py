import random
import unittest
from appium import webdriver
import xmlrunner
import Buttons
import GetCode
import argparse
import sys
import os
from time import sleep
import CreateAccountPage
from tap import TAPTestRunner

#ipad mini 3eb7e0e6de5e265b9c427499c918a43df6da9348
#iphone4 0794eb44a6b3430fd0482878879b5203f460136d
#iPod



def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-device','--device_name',default='3eb7e0e6de5e265b9c427499c918a43df6da9348')
    parser.add_argument('-v','--ios_version',default='8.3')
    parser.add_argument('-l','--link',default='localhost')
    parser.add_argument('-p','--port',default='4723')
    parser.add_argument('-f','--folder',default='ipad')
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
device_name = namespace.device_name
version = namespace.ios_version
port = namespace.port
folder = namespace.port
link = namespace.link

class TestAuto(unittest.TestCase):

    def setUp(self):
        parser = createParser()
        namespace = parser.parse_args(sys.argv[1:])
        device_name = namespace.device_name
        version = namespace.ios_version
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = version
        desired_caps['deviceName'] = device_name
        desired_caps['waitForAppScript'] = '$.delay(35000)'
        desired_caps['uuid']=device_name
        desired_caps['autoAcceptAlerts']=True
        desired_caps['launchTimeout']='350000'
        desired_caps['fullReset']=True
        #desired_caps['noReset']=True
        



        #desired_caps['uuid']='ADBF176E-2D34-4D0F-AB35-97A12D169C54'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'/Users/apium/Documents/Talk-Me-X-5.1.2.ipa'))
        self.driver = webdriver.Remote('http://'+str(link)+':'+ str(port) +'/wd/hub',desired_caps)

        print "set up - OK!"
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
        '''

    def test_iPhone4_SignIn(self):
        print "Test start"
        sleep(1)
        Buttons.Click(self.driver,Buttons.iPhone4_SignIn)
        print "Tap Sign In"
        sleep(2)
        if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text == 'Sign In':
        #if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text == 'Sign In':
            print  "Window: ", self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]').text
            sleep(2)
            facebook_button = self.driver.find_element_by_xpath(Buttons.iPhone4_SignIn_Facebook[0])
            if facebook_button:
                print "Facebook: OK"
                sleep(2)
                if self.driver.find_element_by_name('or').text == 'or':
                    print  "Text: ", self.driver.find_element_by_name('or').text
                    sleep(2)
                    if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[5]').text == 'Sign in with Email or Phone number.':
                        print  "Text: ", self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[5]').text
                        sleep(2)
                        email_phone_field = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
                        if email_phone_field.text == 'EMAIL OR PHONE NUMBER':
                            print  "Text: ", email_phone_field.text
                            sleep(2)
                            email_phone_field.set_value('test@test.test')
                            sleep(2)
                            continue_button = self.driver.find_element_by_xpath(Buttons.iPhone4_SignIn_Continue[0])
                            if continue_button:
                                print "Continue: OK"
                                sleep(2)
                                self.driver.get_screenshot_as_png()
                                self.driver.save_screenshot('/Users/galaninaa/PycharmProjects/untitled/screen.png')
                                continue_button.click()


    def test_iPhone4_SignUp(self):
        print "Test start"
        #sleep(1)
        SignUp = self.driver.find_element_by_name('Sign Up')
        SignUp.click()
        print "Tap Sign Up"
        sleep(2)
        Header = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')
        #Header = self.driver.find_element_by_name('Enter your Phone')
        sleep(5)
        print Header.text
        if Header.text == 'Enter your Phone':
            print  "Window: ", Header.text
            #sleep(2)
            SignUp_text = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]')
            if SignUp_text:
                print "SignUp text: ", SignUp_text.text
                DonTHaveMobile_link = self.driver.find_element_by_name("Don't have a mobile number?")
                if DonTHaveMobile_link.text == "Don't have a mobile number?":
                    print  "Text: ", DonTHaveMobile_link.text
                    #sleep(2)
                    path = '//UIAApplication[1]/UIAWindow[1]/UIATextField[3]'
                    if device_name == '0794eb44a6b3430fd0482878879b5203f460136d':
                        print device_name
                        path = '//UIAApplication[1]/UIAWindow[1]/UIATextField[3]'
                    if self.driver.find_element_by_xpath(Buttons.Ipad_UseMobileNumber):
                        print "This is not a phone"
                        self.driver.find_element_by_xpath(Buttons.Ipad_UseMobileNumber).click()
                    else:
                        print "This is a phone"
                    phone_field = self.driver.find_element_by_xpath(path)
                    if phone_field:
                            print  "Text: ", phone_field.text
                            sleep(2)
                            phone_field.set_value(CreateAccountPage.CreatePhoneNumber())
                            sleep(2)
                            continue_button = self.driver.find_element_by_name('Continue')
                            if continue_button:
                                print "Continue: OK"
                                sleep(2)
                                continue_button.click()
                                sleep(15)
                                #Verification code
                                Header = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]')
                                print Header.text
                                if Header:
                                    sleep(15)
                                    print "In Header..."
                                    #resend_code = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAButton[3]')
                                    #print resend_code.text
                                    #resend_code.click()
                                    print 'I will wait 150 seconds...'
                                    sleep(150)
                                    Message = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]')
                                    if Message:
                                        print 'Message: ', Message.text
                                        #Keys = ['0','1','2','3','4','5','6','7','8','9']
                                        #delete_key = self.driver.find_element_by_name('Delete')
                                        #for key in Keys:
                                        #    print "We will tap keys!.."
                                        #    button = self.driver.find_element_by_name(key)
                                        #    button.click()
                                        #    print "we taped button: ", button.text
                                        #    if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]').text == key:
                                        #        print "Button taped, really: ", button.text
                                        #        delete_key.click()
                                        #        print "We tap delete: ", delete_key.text
                                        #self.driver.find_element_by_name(Keys[1]).click()
                                        #if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[2]').text == Keys[1]:
                                        #    self.driver.find_element_by_name(Keys[2]).click()
                                        #    if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[3]').text == Keys[2]:
                                        #        self.driver.find_element_by_name(Keys[3]).click()
                                        #        if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[4]').text == Keys[3]:
                                        #            self.driver.find_element_by_name(Keys[4]).click()
                                        #            if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[5]').text == Keys[4]:
                                        #                sleep(10)
                                        #                allert = self.driver.switch_to_alert()
                                        #                print 'I see alert:',allert.text
                                        #                sleep(2)
                                        #                allert.accept()
                                        code = GetCode.get_code('/Users/galaninaa/PycharmProjects/untitled/APPIUM.LOG')
                                        print "CODE: ",code
                                        i=2
                                        for digit in code:
                                            button = self.driver.find_element_by_name(digit)
                                            sleep(3)
                                            button.click()
                                            sleep(1)
                                            if self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[' +str(i) +']').text == digit:
                                                print "Button taped, really: ", button.text
                                                i+=1
                                        sleep(10)
                                        self.driver.get_screenshot_as_png()
                                        self.driver.save_screenshot('/Users/galaninaa/PycharmProjects/untitled/screen.png')
                                        print "Cool!"
                                        sleep(5)
                                        CreateAccountPage.AddDataIntoProfile(self.driver)
                                        sleep(10)

        sleep(5)
        self.driver.press_keycode()

    def test_iPhone4_SignUp_different_taps(self):
        print "Test start"
        #sleep(1)
        SignUp = self.driver.find_element_by_name('Sign Up')
        SignUp.click()
        print "Tap Sign Up"
        sleep(2)
        for i in range(1000):
            a=random.randint(1,319)
            b=random.randint(1,319)
            c=random.randint(1,479)
            d=random.randint(1,479)
            print "Step: ",i, ". From (",a,',',c,') to (',b,',',d,')'
            self.driver.swipe(a,c,b,d)
'''

    def test_Ping(self):
        print 'Test'
        sleep (10)
        print 'Test is off'



if __name__ == '__main__':
    print "START!"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner(verbosity=1).run(suite)
    #print "RUN SUITE"
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' + str(folder)))
'''
    # TAP runner
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    loader = unittest.TestLoader() #.loadTestsFromTestCase(ChessAndroidTests)
    tests = loader.loadTestsFromTestCase(TestAuto)
   #discover(tests_dir)
    runner = TAPTestRunner()
    runner.set_outdir('testout')
    runner.set_format('Hi: {method_name} - {short_description}')
    runner.run(tests)
'''