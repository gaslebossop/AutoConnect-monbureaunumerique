from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException
)
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://cas.monbureaunumerique.fr/login?service=https%3A%2F%2Fwww.monbureaunumerique.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT"
REDIRECT_URL = "https://clg-st-remi.monbureaunumerique.fr/sg.do?PROC=PAGE_ACCUEIL&ACTION=VALIDER"


class MonBureauNumeriqueAuth:
    def __init__(self):
        self.driver = None

    def login(self, username, password):
        """Authentifier un utilisateur de manière sécurisée."""
        if not username or not password:
            raise ValueError("Username et password ne peuvent pas être vides")

        if not isinstance(username, str) or not isinstance(password, str):
            raise TypeError("Username et password doivent être des chaînes de caractères")

        try:
            self.driver = webdriver.Chrome()
            logger.info("Connexion au service d'authentification initialisée")

            self.driver.get(BASE_URL)

            self.driver.find_element(By.CLASS_NAME, "form__label").click()
            self.driver.find_element(By.ID, "button-submit").click()
            self.driver.find_element(By.ID, "bouton_eleve").click()

            self.driver.find_element(By.ID, "username").send_keys(username)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.ID, "bouton_valider").click()

            self.driver.get(REDIRECT_URL)
            logger.info("Authentification réussie")
            return True

        except NoSuchElementException as e:
            logger.error(f"Élément HTML non trouvé: {str(e)}")
            raise RuntimeError("Échec de la connexion: interface modifiée ou non accessible")
        except TimeoutException:
            logger.error("Délai d'attente dépassé lors de la connexion")
            raise RuntimeError("Délai d'attente dépassé: le serveur ne répond pas")
        except WebDriverException as e:
            logger.error(f"Erreur du navigateur: {str(e)}")
            raise RuntimeError(f"Erreur technique: impossible d'accéder au service")
        finally:
            if self.driver:
                self.driver.quit()
                logger.info("Ressources du navigateur libérées")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.quit()


def login(username, password):
    """Interface de compatibilité pour l'API existante."""
    auth = MonBureauNumeriqueAuth()
    return auth.login(username, password)

