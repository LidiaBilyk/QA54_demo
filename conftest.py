import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    #The main rule of Selenium: Never mix implicit and explicit waits in the same project.
    # Architecturally, they are implemented at different levels (client-side and browser driver-side).
    # Their combination leads to unpredictable delays: timeouts can accumulate unpredictably, causing "mysterious" test failures.
    # driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()