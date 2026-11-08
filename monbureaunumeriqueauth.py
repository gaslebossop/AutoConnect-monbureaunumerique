from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = None

def _initialize_driver():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.get("https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT")

def login(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("username and password must be strings")
    if not username or not password:
        raise ValueError("username and password cannot be empty")

    _initialize_driver()

    driver.find_element(By.CLASS_NAME, "form__label").click()
    driver.find_element(By.ID, "button-submit").click()
    driver.find_element(By.ID, "bouton_eleve").click()

    elem = driver.find_element(By.ID, "username")
    elem.send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "bouton_valider").click()
    driver.get("https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER")

def close_driver():
    global driver
    if driver is not None:
        driver.quit()
        driver = None

