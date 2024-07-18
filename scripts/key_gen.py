import hashlib
import string
import secrets

"""
Generate a random string of specified length.

Parameters:
- length (int): The length of the random string to generate.

Returns:
- str: A random string of the specified length.

Example:
generate_random_string(10)
'8zKU9gVp6W'
"""

def generate_random_string(length):
    """Generate a random string of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

"""
Generate SHA256 hash of a string.

Parameters:
- input_string (str): The string to hash.

Returns:
- str: The SHA256 hash of the input string.

Example:
generate_sha256_hash('hello world')
'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
"""
def generate_sha256_hash(input_string):
    """Generate SHA256 hash of a string."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()
