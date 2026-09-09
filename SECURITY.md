# Security Guidelines

## Credential Handling

- **Never** hardcode credentials in your code
- **Never** log credentials or sensitive information
- Use environment variables or secure credential storage (e.g., `.env` files with proper `.gitignore`)
- Always handle credentials as strings, never print or debug them

## HTTPS and Certificates

- All connections use HTTPS
- SSL certificates are verified by default in modern Selenium versions
- Ensure your system has up-to-date CA certificates

## Best Practices

1. **Input Validation**: Always validate username and password before passing to `login()`
2. **Error Handling**: Wrap login calls in try-except blocks to handle failures gracefully
3. **Session Management**: Create a new driver instance for each login session
4. **Cleanup**: Always close the browser driver after authentication to free resources
5. **Logging**: Use Python's logging module instead of print statements; never log credentials

## Example Usage

```python
import os
from monbureaunumeriqueauth import login

username = os.getenv("MONBUREAUNUMERIQUE_USERNAME")
password = os.getenv("MONBUREAUNUMERIQUE_PASSWORD")

if not username or not password:
    raise ValueError("Credentials not found in environment variables")

try:
    login(username, password)
except Exception as e:
    print(f"Authentication failed: {e}")
```

## Reporting Security Issues

If you discover a security vulnerability, please report it responsibly to the project maintainers.
