import configparser
import json


def readConfigData(section, Key):
    config = configparser.ConfigParser()
    config.read(r"./Configurations/config.cfg")
    return config.get(section, Key)
    # return key


# print(readConfigData('appConfig', 'testURL'))


def readLocator(locatorPageName, locator_xpath):
    f = open(r"./Configurations/Locators.json")
    data = json.load(f)
    return data[locatorPageName][locator_xpath]
