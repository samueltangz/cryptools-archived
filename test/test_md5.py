import unittest
from cryptools import md5

class TestMD5(unittest.TestCase):
    def setUp(s):
        pass

    def test_hexdigest(self):
        self.assertEqual(md5().hexdigest(), "d41d8cd98f00b204e9800998ecf8427e")
        self.assertEqual(md5("").hexdigest(), "d41d8cd98f00b204e9800998ecf8427e")
        self.assertEqual(md5("Hello, world!").hexdigest(), "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(md5("cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90").hexdigest(), "ea52a276e74e31d07c6f82af2f3c192a")

    def test_digest(self):
        self.assertEqual(md5().digest(), "\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~")
        self.assertEqual(md5("").digest(), "\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t\x98\xec\xf8B~")
        self.assertEqual(md5("Hello, world!").digest(), "l\xd3Um\xeb\r\xa5K\xca\x06\x0bL9G\x989")
        self.assertEqual(md5("cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90").digest(), "\xeaR\xa2v\xe7N1\xd0|o\x82\xaf/<\x19*")
        
