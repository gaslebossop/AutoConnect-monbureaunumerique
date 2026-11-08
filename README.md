# Monbureaunumerique Auth
## Auto connect


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Monbureaunumerique Auth est une librairie python qui permet de se connecter a monbureaunumerique (pour le college saint remi)

- Rapide
- Opensource
- ✨Captcha Bypass

## Features

- AutoConnect

## Installation

Monbureaunumerique Auth requires [Python](https://www.python.org/) to run.

Installer les dependances et importer la librairies .
Exemple : 

```python
import os
from monbureaunumeriqueauth import login, close_driver

# Load credentials from environment variables (secure approach)
username = os.getenv('MONBUREAU_USERNAME')
password = os.getenv('MONBUREAU_PASSWORD')

if not username or not password:
    raise ValueError("Please set MONBUREAU_USERNAME and MONBUREAU_PASSWORD environment variables")

login(username, password)

# Always cleanup the driver when done
close_driver()
```

**Security Note**: Never hardcode credentials in your code. Use environment variables or a secure configuration file instead.




