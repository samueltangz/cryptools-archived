# sha256 hashlib wrapper

from hashlib import sha256

class SHA256(object):
    def __init__(self, text=""):
        self.text = text
        self.hashobj = sha256(text)

    def hexdigest(self):
        return self.hashobj.hexdigest()

    def digest(self):
        return self.hashobj.digest()
