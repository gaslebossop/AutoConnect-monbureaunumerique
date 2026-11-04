from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOGIN_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
DASHBOARD_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"

def _validate_credentials(username, password):
    if not isinstance(username, str) or not username.strip():
        raise ValueError("Username must be a non-empty string")
    if not isinstance(password, str) or not password.strip():
        raise ValueError("Password must be a non-empty string")
    if len(username) > 255 or len(password) > 255:
        raise ValueError("Credentials exceed maximum length")

def login(username, password):
    try:
        _validate_credentials(username, password)

        chrome_options = Options()
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = None

        try:
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(LOGIN_URL)

            driver.find_element(By.CLASS_NAME, "form__label").click()
            driver.find_element(By.ID, "button-submit").click()
            driver.find_element(By.ID, "bouton_eleve").click()

            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)

            driver.find_element(By.ID, "bouton_valider").click()
            driver.get(DASHBOARD_URL)

            logger.info("Login successful")

        finally:
            if driver:
                driver.quit()

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Login failed: {e}")
        raise

