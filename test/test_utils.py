import unittest

from cryptools.utils import *
class TestUtils(unittest.TestCase):
  def setUp(s):
    pass

  def test_convert(self):
    self.assertEqual(convert('Testing', 'str', 'hex'), '54657374696e67')
    self.assertEqual(convert('Testing', 'str', 'b64'), 'VGVzdGluZw==')
    self.assertEqual(convert('Testing', 'str', 'int'), 23755444592406119)
    self.assertEqual(convert('54657374696e67', 'hex', 'str'), 'Testing')
    self.assertEqual(convert('54657374696e67', 'hex', 'b64'), 'VGVzdGluZw==')
    self.assertEqual(convert('54657374696e67', 'hex', 'int'), 23755444592406119)
    self.assertEqual(convert('VGVzdGluZw==', 'b64', 'str'), 'Testing')
    self.assertEqual(convert('VGVzdGluZw==', 'b64', 'hex'), '54657374696e67')
    self.assertEqual(convert('VGVzdGluZw==', 'b64', 'int'), 23755444592406119)
    self.assertEqual(convert(23755444592406119, 'int', 'str'), 'Testing')
    self.assertEqual(convert(23755444592406119, 'int', 'hex'), '54657374696e67')
    self.assertEqual(convert(23755444592406119, 'int', 'b64'), 'VGVzdGluZw==')
