from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOGIN_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
DASHBOARD_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"
TIMEOUT = 10

def _validate_credentials(username, password):
    """Validate that credentials are not empty."""
    if not username or not isinstance(username, str) or len(username.strip()) == 0:
        raise ValueError("Username cannot be empty")
    if not password or not isinstance(password, str) or len(password.strip()) == 0:
        raise ValueError("Password cannot be empty")

def login(username, password):
    """Authenticate to monbureaunumerique portal.

    Args:
        username (str): User's login identifier
        password (str): User's password

    Returns:
        bool: True if login successful, False otherwise

    Raises:
        ValueError: If credentials are invalid
    """
    _validate_credentials(username, password)

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_page_load_timeout(TIMEOUT)

        driver.get(LOGIN_URL)

        try:
            driver.find_element(By.CLASS_NAME, "form__label").click()
            driver.find_element(By.ID, "button-submit").click()
            driver.find_element(By.ID, "bouton_eleve").click()

            username_elem = driver.find_element(By.ID, "username")
            username_elem.send_keys(username)

            password_elem = driver.find_element(By.ID, "password")
            password_elem.send_keys(password)

            driver.find_element(By.ID, "bouton_valider").click()

            time.sleep(2)

            if "erreur" in driver.page_source.lower() or "error" in driver.page_source.lower():
                logger.warning("Login failed: error message detected on page")
                return False

            driver.get(DASHBOARD_URL)

            logger.info("Login successful")
            return True

        except Exception as e:
            logger.error(f"Login process failed: {str(e)}")
            return False

    except Exception as e:
        logger.error(f"WebDriver initialization failed: {str(e)}")
        return False
    finally:
        if driver:
            driver.quit()

