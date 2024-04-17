import pytest
import time


@pytest.mark.skip
def test_test(browser):

    link = 'https://www.wikipedia.org/'
    browser.get(link)

    time.sleep(5)

