from test_rsa import *
from test_utils import *

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TestRSA))
  suite.addTests(unittest.makeSuite(TestUtils))
  return suite