from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app():
    fixture = Application()
    return fixture