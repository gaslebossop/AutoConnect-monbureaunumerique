from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_LOGIN_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
DEFAULT_HOME_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"

class MonBureauNumeriqueAuth:
    def __init__(self, login_url=None, home_url=None):
        self.login_url = login_url or DEFAULT_LOGIN_URL
        self.home_url = home_url or DEFAULT_HOME_URL
        self.driver = None

    def _init_driver(self):
        if self.driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--enable-automation")
            self.driver = webdriver.Chrome(options=chrome_options)

    def _validate_credentials(self, username, password):
        if not username or not isinstance(username, str):
            raise ValueError("Invalid username: must be a non-empty string")
        if not password or not isinstance(password, str):
            raise ValueError("Invalid password: must be a non-empty string")
        if len(username) > 256 or len(password) > 512:
            raise ValueError("Credentials exceed maximum length")

    def login(self, username, password):
        try:
            self._validate_credentials(username, password)
            self._init_driver()

            self.driver.get(self.login_url)

            self.driver.find_element(By.CLASS_NAME, "form__label").click()
            self.driver.find_element(By.ID, "button-submit").click()
            self.driver.find_element(By.ID, "bouton_eleve").click()

            username_elem = self.driver.find_element(By.ID, "username")
            username_elem.send_keys(username)

            password_elem = self.driver.find_element(By.ID, "password")
            password_elem.send_keys(password)

            self.driver.find_element(By.ID, "bouton_valider").click()
            self.driver.get(self.home_url)

            logger.info("Login successful")
            return True
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return False
        except Exception as e:
            logger.error(f"Login failed: {e}")
            return False

    def close(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def __enter__(self):
        self._init_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

