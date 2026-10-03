# Monbureaunumerique Auth
## Auto connect


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Monbureaunumerique Auth est une librairie python qui permet de se connecter a monbureaunumerique (pour le college saint remi)

- Rapide
- Opensource

## Features

- AutoConnect

## Security Notes

- Credentials should be provided via environment variables, not hardcoded
- Always use HTTPS for credential transmission
- Never commit passwords or sensitive data to version control

## Installation

Monbureaunumerique Auth requires [Python](https://www.python.org/) to run.

Installer les dependances et importer la librairies .
Exemple : 

```example
from monbureaunumeriqueauth import login
login("username","password")
```




