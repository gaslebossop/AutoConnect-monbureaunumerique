# Monbureaunumerique Auth
## Auto connect

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Monbureaunumerique Auth est une librairie python qui permet de se connecter a monbureaunumerique (pour le college saint remi)

- Rapide
- Opensource
- Sécurisé

## Features

- AutoConnect avec gestion d'erreurs

## Installation

Monbureaunumerique Auth requires [Python](https://www.python.org/) to run.

Installer les dependances et importer la librairies .
Exemple : 

```python
from monbureaunumeriqueauth import MonBureauNumeriqueAuth

# Utilisation avec context manager (recommandé)
with MonBureauNumeriqueAuth() as auth:
    if auth.login("username", "password"):
        print("Connexion réussie")
    else:
        print("Échec de la connexion")

# Ou utilisation manuelle
auth = MonBureauNumeriqueAuth()
if auth.login("username", "password"):
    print("Connexion réussie")
auth.close()
```

## Security Notes

- Les identifiants sont validés avant utilisation
- Erreurs gérées proprement sans exposition de détails
- Utilisation de Selenium 4+ avec API moderne
- Pas de données sensibles en dur dans le code




