from selenium import webdriver
from selenium.webdriver.common.by import By


def login(username, password):
    driver = webdriver.Chrome()
    try:
        driver.get("https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT")

        driver.find_element(By.CLASS_NAME, "form__label").click()
        driver.find_element(By.ID, "button-submit").click()
        driver.find_element(By.ID, "bouton_eleve").click()

        elem = driver.find_element(By.ID, "username")
        elem.send_keys(username)

        driver.find_element(By.ID, "password").send_keys(password)

        driver.find_element(By.ID, "bouton_valider").click()

        driver.get("https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER")
    finally:
        driver.quit()

