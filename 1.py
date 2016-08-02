import os
import unittest
from appium import webdriver
import xmlrunner
import Buttons
from time import sleep
from tap import TAPTestRunner
 
class TestAuto(unittest.TestCase):

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '8.3'
        desired_caps['deviceName'] = 'iPhone 6 Plus'#3eb7e0e6de5e265b9c427499c918a43df6da9348'#'a96aab872810bd5d925d533869a06b3a174ecaf5'
        desired_caps['waitForAppScript'] = '$.delay(500)'
        #desired_caps['uuid']='3eb7e0e6de5e265b9c427499c918a43df6da9348'
        #desired_caps['uuid']='ADBF176E-2D34-4D0F-AB35-97A12D169C54'
        # Returns abs path relative to this file and not cwd
        #desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'/Users/galaninaa/Library/Developer/Xcode/DerivedData/Talk-Me-X-ddeaozmbhfoptlgkpprcmenjagst/Build/Products/Debug-iphoneos/talkmeim.app'))
        #desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        #desired_caps['appActivity'] = '.ChessFreeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        print "set up - OK!"
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()



 
    '''def test_single_player_mode(self):
        print "Test -OK!"
        sleep(5)
        print "pospal..Teper porabotaem"
        text = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[3]')
        print text.text
        text.click()
        sleep(5)
        text = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[4]')
        print text.text
        text.click()
        sleep(5)
        text = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[5]')
        print text.text
        text.click()
        sleep(5)
        text = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[6]')
        print text.text
        text.click()
        sleep(1)
        text = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAPopover[1]/UIAButton[7]')
        print text.text
        text.click()
        sleep(1)
        print 'I see smth'
        sleep(5)
'''
    def test_TestAuto1(self):
        print "Test start"
        sleep(1)
        print "sleep..."
        Buttons.Click(self.driver,Buttons.Ipad_TabBar_Keypad)
        print "Tap KEYPAD"
        sleep(2)
        ButtonsMass = [Buttons.Ipad_Keypad_1 ,Buttons.Ipad_Keypad_2 ,Buttons.Ipad_Keypad_3 ,Buttons.Ipad_Keypad_4 ,Buttons.Ipad_Keypad_5 ,Buttons.Ipad_Keypad_6 ,Buttons.Ipad_Keypad_7 ,Buttons.Ipad_Keypad_8 ,Buttons.Ipad_Keypad_9 ,Buttons.Ipad_Keypad_0 ,Buttons.Ipad_Keypad_HESH ,Buttons.Ipad_Keypad_STAR]
        for buttons in ButtonsMass:
            Buttons.Click(self.driver,buttons)
        #    sleep(1)
    def test_TestAuto2(self):
        print "Test start"
        sleep(1)
        print "sleep..."
        #Buttons.Click(self.driver,Buttons.Ipad_TabBar_Keypad)
        print "Tap KEYPAD"
        #sleep(2)
        #ButtonsMass = [Buttons.Ipad_Keypad_1 ,Buttons.Ipad_Keypad_2 ,Buttons.Ipad_Keypad_3 ,Buttons.Ipad_Keypad_4 ,Buttons.Ipad_Keypad_5 ,Buttons.Ipad_Keypad_6 ,Buttons.Ipad_Keypad_7 ,Buttons.Ipad_Keypad_8 ,Buttons.Ipad_Keypad_9 ,Buttons.Ipad_Keypad_0 ,Buttons.Ipad_Keypad_HESH ,Buttons.Ipad_Keypad_STAR]
        #for buttons in ButtonsMass:
        #    Buttons.Click(self.driver,buttons)
        #    sleep(1)



if __name__ == '__main__':
    print "START!"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner(verbosity=1).run(suite)
    print "RUN SUITE"
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports'))
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