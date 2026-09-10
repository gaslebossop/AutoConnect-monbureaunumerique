from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(level=logging.WARNING)

def login(username, password):
    if not isinstance(username, str) or not isinstance(password, str):
        raise ValueError("Username and password must be strings")
    if not username or not password:
        raise ValueError("Username and password cannot be empty")

    try:
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT")

        driver.find_element(By.CLASS_NAME, "form__label").click()
        driver.find_element(By.ID, "button-submit").click()
        driver.find_element(By.ID, "bouton_eleve").click()

        elem = driver.find_element(By.ID, "username")
        elem.send_keys(username)

        driver.find_element(By.ID, "password").send_keys(password)

        driver.find_element(By.ID, "bouton_valider").click()

        driver.get("https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER")

        return True
    except Exception as e:
        logging.error("Authentication failed")
        return False
    finally:
        try:
            driver.quit()
        except Exception:
            pass

