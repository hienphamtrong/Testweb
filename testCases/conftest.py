import pytest
from selenium import webdriver

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

#It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'pytest-web-report'
#     config._metadata['Tester'] = 'Hien Pham'

def pytest_configure(config):
    config._metadata['Project Name'] = 'pytest-web-report'
    config._metadata['Tester'] = 'Hien Pham'

# It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
