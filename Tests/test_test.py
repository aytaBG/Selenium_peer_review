import pytest
import time


@pytest.mark.test
def test_test(browser_select):

    link = 'https://www.wikipedia.org/'
    browser_select.get(link)

    time.sleep(5)

