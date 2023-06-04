from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

with open("rsa_1024_priv.pem", "r") as priv_key_file:
  keyString = priv_key_file.read()
  
key = RSA.import_key(keyString)
print(key)

pub_key = key.publickey()
print(pub_key.export_key())

data = "I Love You".encode("utf-8")


# Encrypt the session key with the public RSA key
session_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(pub_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
with open("enc_file.bin", "wb") as enc_file:
  for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext):
    enc_file.write(x)
    
# Decrypt the data with the AES session key
with open("enc_file.bin", "rb") as dec_file:
  enc_session_key, nonce, tag, ciphertext = [dec_file.read(x) for x in (key.size_in_bytes(), 16, 16, -1)]
  

cipher_rsa = PKCS1_OAEP.new(key)
session_key = cipher_rsa.decrypt(enc_session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))