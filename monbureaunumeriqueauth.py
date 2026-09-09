from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://cas.monbureaunumerique.fr/login"
SERVICE_PARAM = "https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
DASHBOARD_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"


def _validate_credentials(username, password):
    if not username or not password:
        raise ValueError("Username and password cannot be empty")
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("Username and password must be strings")


def login(username, password):
    _validate_credentials(username, password)

    driver = None
    try:
        driver = webdriver.Chrome()
        login_url = f"{BASE_URL}?service={SERVICE_PARAM}"
        driver.get(login_url)

        try:
            driver.find_element(By.CLASS_NAME, "form__label").click()
            driver.find_element(By.ID, "button-submit").click()
            driver.find_element(By.ID, "bouton_eleve").click()

            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "bouton_valider").click()

            driver.get(DASHBOARD_URL)
            logger.info("Login successful")

        except NoSuchElementException as e:
            logger.error(f"Login element not found: {e}")
            raise RuntimeError("Failed to locate login elements") from e

    except Exception as e:
        logger.error(f"Login failed: {e}")
        raise
    finally:
        if driver:
            driver.quit()

