from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login(username, password, school="clg-st-remi", timeout=10):
    """
    Authenticate to Monbureaunumerique.

    Args:
        username: User login identifier
        password: User password
        school: School identifier (default: clg-st-remi)
        timeout: Maximum wait time for page elements

    Returns:
        WebDriver: Authenticated browser session

    Raises:
        ValueError: If credentials are invalid or missing
        TimeoutError: If login elements cannot be found
    """
    if not username or not password:
        raise ValueError("Username and password cannot be empty")

    driver = None
    try:
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(timeout)
        wait = WebDriverWait(driver, timeout)

        login_url = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
        driver.get(login_url)

        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form__label"))).click()
            wait.until(EC.element_to_be_clickable((By.ID, "button-submit"))).click()
            wait.until(EC.element_to_be_clickable((By.ID, "bouton_eleve"))).click()

            username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.clear()
            username_field.send_keys(username)

            password_field = driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)

            wait.until(EC.element_to_be_clickable((By.ID, "bouton_valider"))).click()

            home_url = f"https://{school}.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"
            driver.get(home_url)

            return driver

        except Exception as e:
            raise TimeoutError(f"Failed to interact with login page: {str(e)}")

    except Exception as e:
        if driver:
            driver.quit()
        raise


def logout(driver):
    """Safely close the authenticated session."""
    if driver:
        try:
            driver.quit()
        except Exception:
            pass

