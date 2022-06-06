from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time
driver = webdriver.Chrome()
driver.get("https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT")

def login(username, password):

#elem2 = driver.find_element(By.CLASS_NAME,'js-wayf-composant')
#elem2.click()
#driver.find_element_by_id("idp-EDU").click()
    driver.find_element(By.CLASS_NAME, "form__label").click()
    driver.find_element(By.ID, "button-submit").click()
    driver.find_element(By.ID, "bouton_eleve").click()


    elem = driver.find_element_by_id("username")
    elem.send_keys(username)



    driver.find_element_by_id("password").send_keys(password)

    driver.find_element(By.ID, "bouton_valider").click()

    driver.get("https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER")

    #time.sleep(3)
    #driver.quit()
#elem = driver.find_element_by_id("login-password")
#elem.send_keys("MotDePasse1.")

