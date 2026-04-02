import hashlib 
import os
password = "mypassword" 
salt = os.urandom(16)  # Generate a random 16-byte salt 
salted_password = salt + password.encode() 
hash_digest = hashlib.sha256(salted_password).hexdigest()
print(f"Salt: {salt.hex()}") 
print(f"Hash: {hash_digest}")
