# Blum-Goldwasser Probabilistic Encryption

This is a simple program that encrypts and decrypts a message m using the Blum-Goldwasser probabilistic encryption algorithm.
This cryptosystem is a very fast encryption and decryption algorithm, while remaining semantically secure, making it secured against
chosen plaintext attacks. However, Blum-Goldwasser encryption is still not secured agaings chosen ciphertext attacks. If a decryption
"oracle" will decrypt everything we feed it, we can very easily get all necessary `pi`'s to decrypt and encrypt any message with a certain starting seed.

This program is written in Python 2.7. To run simply run

```
python blumgoldwasser.py
```
