# md5 hashlib wrapper

from hashlib import md5

class MD5(object):
    def __init__(self, text=""):
        self.text = text
        self.hashobj = md5(text)
    
    def hexdigest(self):
        return self.hashobj.hexdigest()
