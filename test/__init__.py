from test_rsa import *
from test_utils import *
from test_md5 import *
from test_sha256 import *

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TestRSA))
  suite.addTests(unittest.makeSuite(TestUtils))
  suite.addTests(unittest.makeSuite(TestMD5))
  suite.addTests(unittest.makeSuite(TestSHA256))
  return suite
