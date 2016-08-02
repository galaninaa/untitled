
import unittest
from appium import webdriver
import Fields
import Buttons
import argparse
import sys

from time import sleep

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-device','--device_name',default='e7eddca32184875d43aa17f09e268fb4cfe26eec')
    parser.add_argument('-v','--ios_version',default='8.3')
    parser.add_argument('-l','--link',default='localhost')
    parser.add_argument('-p','--port',default='4727')
    parser.add_argument('-f','--folder',default='ipad')
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
device_name = namespace.device_name
version = namespace.ios_version
port = namespace.port
folder = namespace.port
link = namespace.link

class TestAuto2(unittest.TestCase):

    def setUp2(self):
        parser = createParser()
        namespace = parser.parse_args(sys.argv[1:])
        device_name = namespace.device_name
        version = namespace.ios_version

        desired_caps2 = {}
        desired_caps2['platformName'] = 'iOS'
        desired_caps2['platformVersion'] = '7.0'
        desired_caps2['deviceName'] = '0794eb44a6b3430fd0482878879b5203f460136d'
        desired_caps2['waitForAppScript'] = '$.delay(50000)'
        desired_caps2['uuid']='0794eb44a6b3430fd0482878879b5203f460136d'
        desired_caps2['autoAcceptAlerts']=True
        desired_caps2['launchTimeout']='50000'

        self.driver2 = webdriver.Remote('http://'+str(link)+':'+ '4729' +'/wd/hub',desired_caps2)

        print "set up - OK!"
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
        self.driver2.quit()

    def test_CallFromiPodToiPhone(self):
        print 'Test start:'
        Buttons.TapButtons(self.driver,'Keypad')
        number = '3462009903'
        for digit in number:
            Buttons.TapButtons(self.driver,digit)
        Buttons.TapButtons(self.driver,'make call')
        sleep(10)
        Fields.FindStaticField(self.driver2, 'home: (415) 496-0838')
        Buttons.TapButtons(self.driver2,'accept')
        sleep(10)
        print 'Test passed'


if __name__ == '__main__':
    print "START!"
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAuto)
    print "SUITE"
    unittest.TextTestRunner(verbosity=1).run(suite)
    #print "RUN SUITE"
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='/Users/galaninaa/test-reports/' + str(folder)))

    # TAP runner
    #tests_dir = os.path.dirname(os.path.abspath(__file__))
    #loader = unittest.TestLoader() #.loadTestsFromTestCase(ChessAndroidTests)
    #tests = loader.loadTestsFromTestCase(TestAuto)
   #discover(tests_dir)
    #runner = TAPTestRunner()
    #runner.set_outdir('testout')
    #runner.set_format('Hi: {method_name} - {short_description}')
    #runner.run(tests)
