from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class MonbureaunumeriqueAuth:
    def __init__(self):
        self.driver = None

    def login(self, username, password):
        if not username or not password:
            raise ValueError("Username and password cannot be empty")

        try:
            options = Options()
            self.driver = webdriver.Chrome(options=options)
            self.driver.get("https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT")

            self.driver.find_element(By.CLASS_NAME, "form__label").click()
            self.driver.find_element(By.ID, "button-submit").click()
            self.driver.find_element(By.ID, "bouton_eleve").click()

            elem = self.driver.find_element(By.ID, "username")
            elem.send_keys(username)

            self.driver.find_element(By.ID, "password").send_keys(password)

            self.driver.find_element(By.ID, "bouton_valider").click()

            self.driver.get("https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER")

        except Exception as e:
            raise RuntimeError(f"Login failed: {str(e)}")
        finally:
            if self.driver:
                self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()

