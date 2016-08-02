__author__ = 'galaninaa'
import random
import string
Header = '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]'
FacebookButton = '//UIAApplication[1]/UIAWindow[1]/UIAButton[1]'
FirstName = '//UIAApplication[1]/UIAWindow[1]/UIAImage[2]'
LastName = '//UIAApplication[1]/UIAWindow[1]/UIAImage[4]'
Email = '//UIAApplication[1]/UIAWindow[1]/UIAImage[6]'
Age =  '//UIAApplication[1]/UIAWindow[1]/UIAImage[8]'
Sex = ['//UIAApplication[1]/UIAWindow[1]/UIAButton[3]','//UIAApplication[1]/UIAWindow[1]/UIAButton[4]']
Selected_sex_by_name = ['boy selected','girl selected']
DoneButton = '//UIAApplication[1]/UIAWindow[1]/UIAButton[5]'
Header_SelectAge = '//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAStaticText[1]'
Ages=['//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAButton[8]','//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAButton[7]','//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAButton[6]','//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAButton[5]','//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAButton[4]','//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAButton[3]','//UIAApplication[1]/UIAWindow[3]/UIAActionSheet[1]/UIAButton[2]']


Male_name_data= ['Liam','Noah','Ethan','Mason','Logan','Lucas','Jacob','Jackson','Aiden','Jack','Luke','Elijah','Benjamin','James','William','Michael','Alexander','Oliver','Daniel','Henry','Owen','Gabriel','Matthew','Carter','Ryan','Wyatt','Andrew','Caleb','Jayden','Connor']
Female_name_data = ['Olivia','Emma','Sophia','Ava','Isabella','Mia','Charlotte','Emily','Harper','Abigail','Madison','Avery','Ella','Madison','Lily','Chloe','Sofia','Evelyn','Hannah','Addison','Grace','Zoey','Aubrey','Aria','Zoe','Ellie','Audrey','Natalie','Elizabeth','Scarlett']
LastNames_data = ['Smith','Johnson','Williams','Jones','Brown','Davis','Miller','Wilson','Moore','Taylor','Anderson','Thomas','Jackson','White','Harris','Martin','Thompson','Garcia','Martinez','Robinson','Clark','Rodriguez','Lewis','Lee','Walker','Hall','Allen','Young','Hernandez','King','Wright','Lopez','Hill','Scott','Green','Adams','Baker','Gonzalez','Nelson','Carter','Mitchell','Perez','Roberts','Turner','Phillips','Campbell','Parker','Evans','Edwards','Collins']

def emails():
    result = ''
    for i in range(10):
        result+=str(random.choice(string.ascii_lowercase))
    result+='@'
    for i in range(6):
        result+=str(random.choice(string.ascii_lowercase))
    result+='.com'
    return result

def name_generator(sex):
    if sex == 0: #MALE
        First = random.choice(Male_name_data)
    else:
        First = random.choice(Female_name_data)
    Last = random.choice(LastNames_data)
    result = []
    result.append(First)
    result.append(Last)
    return result

def AddDataIntoProfile(wdriver):
    AccountData = []
    sex = random.randint(0,1)
    Name = name_generator(sex)
    email = emails()
    HowManyAges = random.randint(0,5)
    First_field = wdriver.find_element_by_xpath(FirstName)
    First_field.set_value(Name[0])
    YourFirstName = First_field.text
    AccountData.append(YourFirstName)
    Last_field = wdriver.find_element_by_xpath(LastName)
    Last_field.set_value(Name[1])
    YourLastName = Last_field.text
    AccountData.append(YourLastName)
    email_field = wdriver.find_element_by_xpath(Email)
    email_field.set_value(email)
    YourEmail = email_field.text
    AccountData.append(YourEmail)
    sex_button =wdriver.find_element_by_xpath(Sex[sex])
    sex_button.click()
    if sex == 0:
        YourSex = 'Male'
    else:
        YourSex = 'Female'
    AccountData.append(YourSex)
    Age_field = wdriver.find_element_by_xpath(Age)
    if Age_field:
        Age_field.click()
        Selected_age = wdriver.find_element_by_xpath(Ages[HowManyAges])
        Selected_age.click()
    YourAge = Age_field.text
    AccountData.append(YourAge)
    return AccountData

def CreatePhoneNumber():
    result = '415'
    for i in range(7):
        result+=random.choice(string.digits)
    return result



print CreatePhoneNumber()

