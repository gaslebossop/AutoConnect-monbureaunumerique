# Monbureaunumerique Auth
## Auto Connect

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Monbureaunumerique Auth is a Python library that provides automated authentication to Monbureaunumerique (French educational platform).

**Features:**
- Fast authentication
- Open source
- Secure credential handling
- Support for multiple schools
- Session management

## Security

This library uses Selenium WebDriver for browser automation. **Passwords should never be stored in code or logs.** Always use environment variables or secure credential stores.

## Installation

Requires [Python](https://www.python.org/) 3.6+ and [Selenium](https://selenium.dev/) 4+.

```bash
pip install selenium
```

## Usage

```python
from monbureaunumeriqueauth import login, logout
import os

# Get credentials from environment variables
username = os.getenv("MBN_USERNAME")
password = os.getenv("MBN_PASSWORD")
school = os.getenv("MBN_SCHOOL", "clg-st-remi")

try:
    driver = login(username, password, school=school)
    
    # Your automation code here
    # driver.find_element(...)
    
    logout(driver)
except ValueError as e:
    print(f"Invalid credentials: {e}")
except TimeoutError as e:
    print(f"Login failed: {e}")
```

## Parameters

- `username` (str): User login identifier
- `password` (str): User password
- `school` (str, optional): School identifier. Default: "clg-st-remi"
- `timeout` (int, optional): Maximum wait time for page elements in seconds. Default: 10

## Error Handling

- `ValueError`: Raised if credentials are empty
- `TimeoutError`: Raised if login elements cannot be found within timeout period

## License

This project is open source.




