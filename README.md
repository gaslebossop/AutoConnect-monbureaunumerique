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

Monbureaunumerique Auth requires [Python](https://www.python.org/) v3.6+ and Selenium to run.

Install dependencies:
```bash
pip install selenium
```

Import and use the library:
```python
from monbureaunumeriqueauth import login

# Never hardcode credentials - use environment variables or secure input
login("username", "password")
```

## Security Best Practices

⚠️ **IMPORTANT SECURITY INFORMATION**

1. **Never hardcode credentials** in your source code
2. **Use environment variables** to pass sensitive information:
   ```python
   import os
   from monbureaunumeriqueauth import login
   
   username = os.getenv('MONBUREAUNUMERIQUE_USERNAME')
   password = os.getenv('MONBUREAUNUMERIQUE_PASSWORD')
   login(username, password)
   ```

3. **Store credentials securely** using a password manager or secrets management system
4. **Keep dependencies updated** to ensure security patches are applied
5. **Never commit `.env` files** to version control
6. **Use HTTPS only** for all communications
7. **Clear sensitive data** from memory when no longer needed

## Requirements

- Python 3.6+
- Selenium
- Chrome/Chromium browser with chromedriver




