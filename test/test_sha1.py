import unittest
from cryptools import sha1

class TestSHA1(unittest.TestCase):
    def setUp(s):
        pass

    def test_hexdigest(self):
        self.assertEqual(sha1().hexdigest(), "da39a3ee5e6b4b0d3255bfef95601890afd80709")
        self.assertEqual(sha1("").hexdigest(), "da39a3ee5e6b4b0d3255bfef95601890afd80709")
        self.assertEqual(sha1("Hello, world!").hexdigest(), "943a702d06f34599aee1f8da8ef9f7296031d699")
        self.assertEqual(sha1("cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90").hexdigest(), "529147eb21d5dc689a243543d344815780eeebd3")

    def test_digest(self):
        self.assertEqual(sha1().digest(), "\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90\xaf\xd8\x07\t")
        self.assertEqual(sha1("").digest(), "\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90\xaf\xd8\x07\t")
        self.assertEqual(sha1("Hello, world!").digest(), "\x94:p-\x06\xf3E\x99\xae\xe1\xf8\xda\x8e\xf9\xf7)`1\xd6\x99")
        self.assertEqual(sha1("cf80cd8aed482d5d1527d7dc72fceff84e6326592848447d2dc0b0e87dfc9a90").digest(), "R\x91G\xeb!\xd5\xdch\x9a$5C\xd3D\x81W\x80\xee\xeb\xd3")
