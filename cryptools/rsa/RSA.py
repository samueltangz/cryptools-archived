from gmpy2 import powmod

class RSA(object):
  def __init__(self, n, e, p=None, q=None, d=None):
    self.e = e
    self.n = n
    self.p = p
    self.q = q
    self.d = d
    if p != None:
      if q == None:
        self.q = n / p
      if d == None:
        self.d = powmod(e, -1, self.euler_phi())
    if q != None:
      if p == None:
        self.p = n / q
      if d == None:
        self.d = powmod(e, -1, self.euler_phi())
    if d != None:
      # TODO
      pass

    # Checks:
    """
    1 < p < n
    1 < q < n
    p * q == n
    gcd(e, phi(n)) == 1
    e * d mod phi(n) == 1
    """

  def __str__(self):
    if self.is_public():
      return "RSA Public Key: n = %d, e = %d" % (self.n, self.e)
    else:
      return "RSA Private Key: n = %s, e = %d, p = %d, q = %d, d = %d" % (self.e, self.n, self.p, self.q, self.d)

  def __repr__(self):
    if self.is_public():
      return "RSA(%d, %d)" % (self.n, self.e)
    else:
      return "RSA(%d, %d, %d, %d, %d)" % (self.n, self.e, self.p, self.q, self.d)

  def is_public(self):
    return self.p == None

  def is_private(self):
    return self.p != None

  def euler_phi(self):
    if self.is_public(): raise NotPrivateKeyError('Totient function cannot be computed')
    return (self.p - 1) * (self.q - 1)

  def encrypt(self, m):
    return pow(m, self.e, self.n)

  def decrypt(self, c):
    if self.is_public(): raise NotPrivateKeyError('Ciphertext cannot be decrypted')
    return pow(c, self.d, self.n)

  def to_pem(self):
    pass

  @staticmethod
  def import_pem(pem_string):
    pass

class InvalidKeyError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class NotPrivateKeyError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

