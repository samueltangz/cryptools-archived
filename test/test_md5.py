import unittest
from cryptools import md5

class TestMD5(unittest.TestCase):
    def setUp(s):
        pass

    def test_digest(self):
        self.assertEqual(md5().hexdigest(), "d41d8cd98f00b204e9800998ecf8427e")
        self.assertEqual(md5("").hexdigest(), "d41d8cd98f00b204e9800998ecf8427e")
        self.assertEqual(md5("Hello, world!").hexdigest(), "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(md5("cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90").hexdigest(), "ea52a276e74e31d07c6f82af2f3c192a")
