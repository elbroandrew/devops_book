import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


secret = "This is the secret password"
bsecret = secret.encode()  # convert to binary string

m = hashlib.md5()
m.update(bsecret)

print(m.digest())

# example with cryptography Fernet (AES algo)
key = Fernet.generate_key()
print(key)
# encrypt the data using Fernet object (to store the key)
f = Fernet(key)
message = b'Hello World'
encrypted = f.encrypt(message)
print(encrypted)
# decrypt
print(f.decrypt(encrypted))

# pair hashing with public and private keys
# use private key to decrypt messages encrypted with public key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,
    backend=default_backend()
)

public_key = private_key.public_key()
message2 = b'Hello World'
encrypted2 = public_key.encrypt(
    message,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None
                 )
)

decrypted2 = private_key.decrypt(
    encrypted2,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm=hashes.SHA256(),
                 label=None
                 )
)
print(decrypted2)
















