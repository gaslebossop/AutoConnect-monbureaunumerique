from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

LOGIN_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
HOME_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"

def login(username, password):
	if not isinstance(username, str) or not isinstance(password, str):
		raise ValueError("Username and password must be strings")
	if not username or not password:
		raise ValueError("Username and password cannot be empty")

	driver = webdriver.Chrome()
	wait = WebDriverWait(driver, 10)

	try:
		driver.get(LOGIN_URL)

		wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form__label"))).click()
		wait.until(EC.presence_of_element_located((By.ID, "button-submit"))).click()
		wait.until(EC.presence_of_element_located((By.ID, "bouton_eleve"))).click()

		username_elem = wait.until(EC.presence_of_element_located((By.ID, "username")))
		username_elem.send_keys(username)

		password_elem = wait.until(EC.presence_of_element_located((By.ID, "password")))
		password_elem.send_keys(password)

		wait.until(EC.presence_of_element_located((By.ID, "bouton_valider"))).click()

		driver.get(HOME_URL)

	except Exception as e:
		print(f"Login failed: {str(e)}")
		raise
	finally:
		driver.quit()
