# from selene.support.shared import browser
# from selene import be, have
import pytest


# browser.open('https://google.com')
# browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

@pytest.fixture(scope='session', autouse=True)
def before_all(request):
    print("Called before all tests: " + request.node.name)


def test_first(before_all):
    assert 1 == 1
