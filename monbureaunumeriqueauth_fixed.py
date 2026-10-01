from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import sys
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MonbureaunumeriqueAuth:
    """Secure authentication handler for Monbureaunumerique"""

    DEFAULT_LOGIN_URL = "https://cas.monbureaunumerique.fr/login"
    DEFAULT_SERVICE_URL = "https://www.monbureaunumerique.fr/sg.do?PROC=IDENTIFICATION_FRONT"
    DEFAULT_HOME_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"
    TIMEOUT = 10

    def __init__(self, headless: bool = False):
        """Initialize authentication handler with optional headless mode"""
        self.driver: Optional[webdriver.Chrome] = None
        self.headless = headless

    def _init_driver(self):
        """Initialize Chrome WebDriver with security-focused options"""
        if self.driver is not None:
            return

        options = Options()
        if self.headless:
            options.add_argument("--headless")

        # Security-focused options
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.set_page_load_timeout(self.TIMEOUT)
        except Exception as e:
            logger.error(f"Failed to initialize WebDriver: {e}")
            raise

    def _validate_credentials(self, username: str, password: str) -> None:
        """Validate input credentials"""
        if not username or not isinstance(username, str):
            raise ValueError("Username must be a non-empty string")
        if not password or not isinstance(password, str):
            raise ValueError("Password must be a non-empty string")
        if len(username) > 255 or len(password) > 255:
            raise ValueError("Credentials exceed maximum length")

    def _wait_for_element(self, by: By, value: str, timeout: int = None) -> None:
        """Safely wait for and find element with timeout"""
        timeout = timeout or self.TIMEOUT
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return self.driver.find_element(by, value)
        except Exception as e:
            logger.error(f"Timeout waiting for element {value}: {e}")
            raise

    def login(self, username: str, password: str) -> bool:
        """
        Authenticate with Monbureaunumerique

        Args:
            username: User's login name
            password: User's password (should not be logged)

        Returns:
            bool: True if login successful, False otherwise

        Raises:
            ValueError: If credentials are invalid
            Exception: If WebDriver operations fail
        """
        try:
            self._validate_credentials(username, password)
            self._init_driver()

            # Navigate to login page
            login_url = f"{self.DEFAULT_LOGIN_URL}?service={self._urlencode(self.DEFAULT_SERVICE_URL)}"
            self.driver.get(login_url)

            # Click on form label
            form_label = self._wait_for_element(By.CLASS_NAME, "form__label")
            form_label.click()

            # Submit button
            submit_btn = self._wait_for_element(By.ID, "button-submit")
            submit_btn.click()

            # Student button
            student_btn = self._wait_for_element(By.ID, "bouton_eleve")
            student_btn.click()

            # Enter username
            username_field = self._wait_for_element(By.ID, "username")
            username_field.clear()
            username_field.send_keys(username)

            # Enter password
            password_field = self._wait_for_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)

            # Validate button
            validate_btn = self._wait_for_element(By.ID, "bouton_valider")
            validate_btn.click()

            # Navigate to home page
            self.driver.get(self.DEFAULT_HOME_URL)

            logger.info("Login successful")
            return True

        except ValueError as e:
            logger.error(f"Invalid credentials: {e}")
            raise
        except Exception as e:
            logger.error(f"Login failed: {e}")
            return False

    @staticmethod
    def _urlencode(url: str) -> str:
        """URL encode a string"""
        from urllib.parse import quote
        return quote(url, safe='')

    def quit(self) -> None:
        """Clean up and close WebDriver"""
        if self.driver:
            try:
                self.driver.quit()
                self.driver = None
            except Exception as e:
                logger.warning(f"Error closing driver: {e}")

    def __enter__(self):
        """Context manager entry"""
        self._init_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.quit()


# Backward compatibility function
def login(username: str, password: str) -> bool:
    """Legacy login function - use MonbureaunumeriqueAuth class instead"""
    auth = MonbureaunumeriqueAuth()
    try:
        return auth.login(username, password)
    finally:
        auth.quit()
