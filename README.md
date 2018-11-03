cryptools
===

A Python module with common cryptographic attacks


## Installation and Testing

```bash
sudo python setup.py install # Install
python setup.py test # Test
```


## Features

### Basic implementations

* Utilty functions
    1. Type conversion (Base64, hex, string, integer, ...)
    2. **TODO** Math functions (gcd, mod inverse, ...)
* Symmetric cipher encryptions (Wrapping libraries)
    * Algorithms
        1. **TODO** DES
        2. **TODO** AES
    * Modes of operations
        1. **TODO** ECB
        2. **TODO** CBC
    * Padding schemes
        1. **TODO** PKCS#7
* Asymmetric cipher encryptions
    * Algorithms
        1. RSA
        2. **TODO** Paillier
* Hash algorithms
    1. **TODO** MD5
    2. **TODO** SHA1
    3. **TODO** SHA2
* Random numbers
    1. **TODO** Linear congruential generator
    2. **TODO** Mersenne twist

### Attacks

* RSA attacks
    1. **TODO** Obtain p, q when given e, d, n
    2. **TODO** Common modulus attack
    3. **TODO** Wiener attack
    4. **TODO** Broadcast attack
    5. **TODO** Coppersmith attack
    6. **TODO** Partial key exposure
    7. **TODO** Bleichenbacher's million message attack
    8. **TODO** LSB oracle
* Block cipher attacks
    1. **TODO** Padding oracle for CBC
* Hash attacks
    1. **TODO** Length extension attack for Merkle-Damgard scheme hashes
* Random numbers attack
    1. **TODO** Recovering LCG
    2. **TODO** Recovering MT19937 with internal states