from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CAS_LOGIN_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
DASHBOARD_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"
TIMEOUT = 10

def login(username, password):
    """
    Authenticate with MonBureauNumerique.

    Args:
        username: User login credentials
        password: User password (never logged)

    Raises:
        ValueError: If username/password are invalid
        TimeoutError: If page elements don't load
    """
    if not username or not password:
        raise ValueError("Username and password cannot be empty")

    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get(CAS_LOGIN_URL)

        wait = WebDriverWait(driver, TIMEOUT)

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form__label"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "button-submit"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "bouton_eleve"))).click()

        username_elem = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_elem.send_keys(username)

        password_elem = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_elem.send_keys(password)

        wait.until(EC.element_to_be_clickable((By.ID, "bouton_valider"))).click()

        driver.get(DASHBOARD_URL)

        logger.info("Login successful")
        return True

    except Exception as e:
        logger.error(f"Login failed: {type(e).__name__}")
        raise
    finally:
        if driver:
            driver.quit()
