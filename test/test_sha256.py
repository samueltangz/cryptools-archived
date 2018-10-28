import unittest

from cryptools import sha256

class TestSHA256(unittest.TestCase):
    def setUp(s):
        pass

    def test_digest(self):
        self.assertEqual(sha256().hexdigest(), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        self.assertEqual(sha256("").hexdigest(), "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
        self.assertEqual(sha256("Hello, world!").hexdigest(), "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3")
        self.assertEqual(sha256("testing").hexdigest(), "cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90")
