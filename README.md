# Monbureaunumerique Auth
## Auto connect

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Monbureaunumerique Auth est une librairie python qui permet de se connecter a monbureaunumerique (pour le college saint remi)

- Rapide
- Opensource
- ✨Captcha Bypass

## Features

- AutoConnect
- Input validation and error handling
- Secure credential handling
- Proper resource cleanup

## Installation

Monbureaunumerique Auth requires [Python](https://www.python.org/) and [Selenium](https://www.selenium.dev/) to run.

Installer les dependances et importer la librairies.
Exemple : 

```python
from monbureaunumeriqueauth import login, close_driver

# Login with your credentials
success = login("your_username", "your_password")

if success:
    print("Login successful!")
else:
    print("Login failed!")

# Always close the driver when done
close_driver()
```

## Security Notes

⚠️ **Important**: Never hardcode credentials in your application. Use environment variables or secure credential management systems instead.

```python
import os
from monbureaunumeriqueauth import login, close_driver

username = os.getenv("MONBUREAUNUMERIQUE_USERNAME")
password = os.getenv("MONBUREAUNUMERIQUE_PASSWORD")

if username and password:
    success = login(username, password)
    close_driver()
```




