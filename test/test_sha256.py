import unittest

from cryptools import sha256

class TestSHA256(unittest.TestCase):
    def setUp(s):
        pass

    def test_hexdigest(self):
        self.assertEqual(sha256().hexdigest(), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        self.assertEqual(sha256("").hexdigest(), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        self.assertEqual(sha256("Hello, world!").hexdigest(), "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3")
        self.assertEqual(sha256("testing").hexdigest(), "cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90")

    def test_digest(self):
        self.assertEqual(sha256().digest(), "\xe3\xb0\xc4B\x98\xfc\x1c\x14\x9a\xfb\xf4\xc8\x99o\xb9$'\xaeA\xe4d\x9b\x93L\xa4\x95\x99\x1bxR\xb8U")
        self.assertEqual(sha256("").digest(), "\xe3\xb0\xc4B\x98\xfc\x1c\x14\x9a\xfb\xf4\xc8\x99o\xb9$'\xaeA\xe4d\x9b\x93L\xa4\x95\x99\x1bxR\xb8U")
        self.assertEqual(sha256("Hello, world!").digest(), "1_[\xdbv\xd0x\xc4;\x8a\xc0\x06NJ\x01da+\x1f\xcew\xc8i4[\xfc\x94\xc7X\x94\xed\xd3")
        self.assertEqual(sha256("testing").digest(), "\xcf\x80\xcd\x8a\xedH-]\x15'\xd7\xdcr\xfc\xef\xf8Nc&Y(HD}-\xc0\xb0\xe8}\xfc\x9a\x90")
