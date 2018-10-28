import unittest
from gmpy2 import powmod

from cryptools import RSA
class TestRSA(unittest.TestCase):
  def setUp(self):
    pass

  # Basic object testing
  def test_object(self):
    p = 10**9 + 7
    q = 10**9 + 9
    n = p * q
    e = 65537
    d = 648946405777194593

    rsa = RSA(n, e)
    self.assertTrue(rsa.is_public())
    self.assertFalse(rsa.is_private())
    self.assertEqual(rsa.n, n)
    self.assertEqual(rsa.e, e)
    self.assertEqual(rsa.encrypt(1), 1)

    '''
    rsa = RSA(n, e, d=d)
    self.assertFalse(rsa.is_public())
    self.assertTrue(rsa.is_private())
    self.assertEqual(rsa.n, n)
    self.assertEqual(rsa.e, e)
    self.assertEqual(rsa.d, d)
    self.assertGreater(rsa.p, 1)
    self.assertGreater(rsa.q, 1)
    self.assertEqual(rsa.p * rsa.q, n)
    self.assertEqual(rsa.encrypt(1), 1)
    self.assertEqual(rsa.decrypt(1), 1)
    '''

    rsa = RSA(n, e, p=p)
    self.assertFalse(rsa.is_public())
    self.assertTrue(rsa.is_private())
    self.assertEqual(rsa.n, n)
    self.assertEqual(rsa.e, e)
    self.assertEqual(rsa.d, d)
    self.assertEqual(rsa.p, p)
    self.assertEqual(rsa.q, n / p)
    self.assertEqual(rsa.encrypt(1), 1)
    self.assertEqual(rsa.decrypt(1), 1)

    # PEM and object conversion
    '''
    rsa = RSA.import_pem('-----BEGIN PUBLIC KEY-----\nMBswDQYJKoZIhvcNAQEBBQADCgAwBwICAUMCAQc=\n-----END PUBLIC KEY-----')
    self.assertTrue(rsa.is_public())
    self.assertFalse(rsa.is_private())
    self.assertEqual(rsa.n, n)
    self.assertEqual(rsa.e, e)
    self.assertEqual(rsa.encrypt(1), 1)
    '''
    # Import a private key
    # rsa.to_pem()
    # Export a public key
    # Export a private key
