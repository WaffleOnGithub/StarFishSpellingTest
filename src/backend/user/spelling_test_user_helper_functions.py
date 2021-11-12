"""
Edited by: Jacob
Date edited: 12/11/21

Helper functions for login/register
"""

import hashlib  # Used to hash passwords


def hash_password(password, salt):
    """
    Helper function for register that hashes a password

    :returns: hashed key with salt
    """

    # Hashes password
    key = hashlib.pbkdf2_hmac(
        "sha256",  # Hash digest algorithm
        password.encode("utf-8"),  # Convert password to bytes
        salt,
        100000  # Iterations of hash digest algorithm
    )

    # Return salt and hashed password together
    return salt + key
