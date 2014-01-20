
def extract_string(value):
  if not (value and value[0] == value[-1] and value[0] in ('"', "'")):
    return value
  return value[1:-1]
