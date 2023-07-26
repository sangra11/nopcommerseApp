from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching Chrome browser.......")
    elif browser=='firefox':
        driver = webdriver.firefox()
        print("Launching Firefox browser......")
    return driver


def pytest_addoption(parser):         #This will get thevalue from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       #This will return the browser value to setup method
    return request.config.getoption("--browser")


########### Pytest HTML Reports ###############

# It is hook for Adding Enviroment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Custmores'
    config._metadata['Tester'] = 'Sangram'

# It is hook for delete/Modify Envoirment info to HTML Report

@pytest.mark.optionlhook
def pytest_metadata(metadata):
    metadata.pop("Java_HOME", None)
    metadata.pop("plugins", None)