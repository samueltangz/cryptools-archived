cryptools
===

A Python module with common cryptographic attacks


## Installation and Testing

```bash
sudo python setup.py install # Install
python setup.py test # Test
```


## To-do

### Basic implementations

* Utilty functions
    1. Type conversion (Base64, hex, string, integer, ...)
    2. Math functions (gcd, mod inverse, ...)
* Symmetric cipher encryptions (Wrapping libraries)
    * Algorithms
        1. DES / AES
    * Modes of operations
        1. ECB / CBC
    * Padding schemes
        1. PKCS#7
* Asymmetric cipher encryptions
    * Algorithms
        1. RSA / Paillier
* Hash algorithms
    1. MD5 / SHA1 / SHA2

### Attacks

* RSA attacks
    1. Obtain p, q when given e, d, n
    2. Common modulus attack
    3. Wiener attack
    4. Broadcast attack / Coppersmith attack
    5. Partial key exposure
    6. Bleichenbacher's million message attack
    7. LSB oracle
* Block cipher attacks
    1. Bit-flipping attack for CBC
    2. Padding oracle for CBC
* Hash attacks
    1. Length extension attack for Merkle-Damgard scheme hashes
