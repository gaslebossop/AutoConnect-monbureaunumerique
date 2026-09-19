from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOGIN_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
DASHBOARD_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"
TIMEOUT = 10

driver: Optional[webdriver.Chrome] = None

def _initialize_driver() -> webdriver.Chrome:
    global driver
    if driver is not None:
        return driver

    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def _validate_credentials(username: str, password: str) -> bool:
    if not username or not password:
        raise ValueError("Username and password cannot be empty")
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("Username and password must be strings")
    if len(username) > 256 or len(password) > 256:
        raise ValueError("Credentials exceed maximum length")
    return True

def login(username: str, password: str) -> bool:
    try:
        _validate_credentials(username, password)

        drv = _initialize_driver()
        drv.get(LOGIN_URL)

        wait = WebDriverWait(drv, TIMEOUT)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form__label"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "button-submit"))).click()
        wait.until(EC.presence_of_element_located((By.ID, "bouton_eleve"))).click()

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.clear()
        username_field.send_keys(username)

        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(password)

        wait.until(EC.presence_of_element_located((By.ID, "bouton_valider"))).click()

        drv.get(DASHBOARD_URL)
        logger.info("Login successful")
        return True

    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        return False

def close_driver() -> None:
    global driver
    if driver is not None:
        driver.quit()
        driver = None
        logger.info("Driver closed")

