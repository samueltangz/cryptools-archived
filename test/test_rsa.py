import unittest
from gmpy2 import powmod

from cryptools import RSA
class TestRSA(unittest.TestCase):
  def setUp(s):
    pass

  # Basic object testing
  def test_object(s):
    p = 10**9 + 7
    q = 10**9 + 9
    n = p * q
    e = 65537
    d = 648946405777194593

    rsa = RSA(n, e)
    s.assertTrue(rsa.is_public())
    s.assertFalse(rsa.is_private())
    s.assertEqual(rsa.n, n)
    s.assertEqual(rsa.e, e)
    s.assertEqual(rsa.encrypt(1), 1)

    '''
    rsa = RSA(n, e, d=d)
    s.assertFalse(rsa.is_public())
    s.assertTrue(rsa.is_private())
    s.assertEqual(rsa.n, n)
    s.assertEqual(rsa.e, e)
    s.assertEqual(rsa.d, d)
    s.assertGreater(rsa.p, 1)
    s.assertGreater(rsa.q, 1)
    s.assertEqual(rsa.p * rsa.q, n)
    s.assertEqual(rsa.encrypt(1), 1)
    s.assertEqual(rsa.decrypt(1), 1)
    '''

    rsa = RSA(n, e, p=p)
    s.assertFalse(rsa.is_public())
    s.assertTrue(rsa.is_private())
    s.assertEqual(rsa.n, n)
    s.assertEqual(rsa.e, e)
    s.assertEqual(rsa.d, d)
    s.assertEqual(rsa.p, p)
    s.assertEqual(rsa.q, n / p)
    s.assertEqual(rsa.encrypt(1), 1)
    s.assertEqual(rsa.decrypt(1), 1)

    # PEM and object conversion
    '''
    rsa = RSA.import_pem('-----BEGIN PUBLIC KEY-----\nMBswDQYJKoZIhvcNAQEBBQADCgAwBwICAUMCAQc=\n-----END PUBLIC KEY-----')
    s.assertTrue(rsa.is_public())
    s.assertFalse(rsa.is_private())
    s.assertEqual(rsa.n, n)
    s.assertEqual(rsa.e, e)
    s.assertEqual(rsa.encrypt(1), 1)
    '''
    # Import a private key
    # rsa.to_pem()
    # Export a public key
    # Export a private key

  def test_(s):
    pass