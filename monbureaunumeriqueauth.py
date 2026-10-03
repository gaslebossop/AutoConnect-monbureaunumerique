from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from typing import Optional


def login(username: str, password: str) -> Optional[webdriver.Chrome]:
    """
    Login to monbureaunumerique service.

    Args:
        username: User's username (should be from environment or secure input)
        password: User's password (should be from environment or secure input)

    Returns:
        WebDriver instance or None if login fails

    Raises:
        ValueError: If username or password are empty/invalid
        Exception: If Selenium driver initialization fails
    """
    if not username or not password:
        raise ValueError("Username and password cannot be empty")

    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("Username and password must be strings")

    try:
        driver = webdriver.Chrome()
        driver.get("https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT")

        driver.find_element(By.CLASS_NAME, "form__label").click()
        driver.find_element(By.ID, "button-submit").click()
        driver.find_element(By.ID, "bouton_eleve").click()

        elem = driver.find_element(By.ID, "username")
        elem.send_keys(username)

        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "bouton_valider").click()

        driver.get("https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER")

        return driver

    except Exception as e:
        print(f"Login failed: {type(e).__name__}")
        raise

