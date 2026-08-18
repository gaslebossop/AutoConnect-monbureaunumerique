from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

LOGIN_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
DASHBOARD_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"
TIMEOUT = 10


def login(username, password):
    if not username or not password:
        raise ValueError("Username and password must not be empty")

    driver = webdriver.Chrome()
    try:
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, TIMEOUT)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form__label"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "button-submit"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "bouton_eleve"))).click()

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys(username)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)

        wait.until(EC.presence_of_element_located((By.ID, "bouton_valider"))).click()

        driver.get(DASHBOARD_URL)

    except Exception as e:
        logger.error("Login failed: %s", str(e))
        raise
    finally:
        driver.quit()

