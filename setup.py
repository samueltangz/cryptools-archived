from setuptools import setup, find_packages

setup(name='cryptools',
  version='0.0.1',
  description='A Python module with common cryptographic attacks',
  author='0x000505AD',
  url='https://github.com/samueltangz/cryptools',
  packages=find_packages(),
  test_suite='test.suite',
  install_requires=[
    'gmpy2',
    'pycrypto'
  ]
)