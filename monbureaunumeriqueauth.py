from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MonbureaunumeriqueAuth:
    def __init__(self, school_domain="clg-st-remi"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.school_domain = school_domain
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        if not username or not password:
            raise ValueError("Username and password cannot be empty")

        try:
            login_url = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
            self.driver.get(login_url)

            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form__label"))).click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "button-submit"))).click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "bouton_eleve"))).click()

            username_field = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.send_keys(username)

            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_field.send_keys(password)

            self.wait.until(EC.element_to_be_clickable((By.ID, "bouton_valider"))).click()

            dashboard_url = f"https://{self.school_domain}.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"
            self.driver.get(dashboard_url)

        except Exception as e:
            self.cleanup()
            raise RuntimeError(f"Login failed: {str(e)}") from e

    def cleanup(self):
        if self.driver:
            try:
                self.driver.quit()
            except Exception as e:
                print(f"Error closing driver: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()


def login(username, password, school_domain="clg-st-remi"):
    auth = MonbureaunumeriqueAuth(school_domain)
    try:
        auth.login(username, password)
        return auth
    except Exception:
        auth.cleanup()
        raise

