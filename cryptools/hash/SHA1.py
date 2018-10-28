# sha1 hashlib wrapper

from hashlib import sha1

class SHA1(object):
    def __init__(self, text=""):
        self.text = text
        self.hashobj = sha1(text)

    def hexdigest(self):
        return self.hashobj.hexdigest()

    def digest(self):
        return self.hashobj.digest()
