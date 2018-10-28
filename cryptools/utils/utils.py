import base64

def convert(payload, from_type=None, to_type=None):
  if from_type == None: from_type = 'str'
  if to_type == None: to_type = 'str'

  if from_type == 'hex':
    if len(payload) % 2 == 1: payload = '0' + payload
    return convert(payload.decode('hex'), None, to_type)
  elif from_type == 'b64':
    return convert(base64.b64decode(payload), None, to_type)
  elif from_type == 'int':
    return convert(format(payload, 'x'), 'hex', to_type)
  elif from_type == 'str':
    pass
  else:
    raise TypeNotImplementedError(from_type)

  if to_type == 'hex':
    return payload.encode('hex')
  elif to_type == 'b64':
    return base64.b64encode(payload)
  elif to_type == 'int':
    return int(payload.encode('hex'), 16)
  elif to_type == 'str':
    return payload
  else:
    raise TypeNotImplementedError(to_type)

class TypeNotImplementedError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)