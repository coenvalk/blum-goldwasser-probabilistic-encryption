# Blum-Goldwasser Probabilistic Encryption

This is a simple program that encrypts and decrypts a message m using the Blum-Goldwasser probabilistic encryption algorithm.
This cryptosystem is a very fast encryption and decryption algorithm, while remaining semantically secure, making it secured against
chosen plaintext attacks. However, Blum-Goldwasser encryption is still not secured agaings chosen ciphertext attacks. If a decryption
"oracle" will decrypt everything we feed it, we can gain information about the seed `x0`, `p`, and `q`.

This program is written in Python 2.7. To run simply run

```
python blumgoldwasser.py
```
