from test_rsa import *

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(TestRSA))
  return suite