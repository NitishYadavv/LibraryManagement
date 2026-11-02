import pytest
import threading
from app import app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from werkzeug.serving import make_server

@pytest.fixture(scope="module")
def server():
    server = make_server("127.0.0.1", 5001, app)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    yield
    server.shutdown()
    thread.join()

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_successful_login(server, browser):
    browser.get("http://127.0.0.1:5001/login")
    browser.find_element(By.ID, "username").send_keys("admin")
    browser.find_element(By.ID, "password").send_keys("1234")
    browser.find_element(By.ID, "login").click()
    assert "Login Successful" in browser.page_source

def test_invalid_login(server, browser):
    browser.get("http://127.0.0.1:5001/login")
    browser.find_element(By.ID, "username").send_keys("wrong")
    browser.find_element(By.ID, "password").send_keys("wrong")
    browser.find_element(By.ID, "login").click()
    assert "Invalid Credentials" in browser.page_source
