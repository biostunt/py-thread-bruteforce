import hashlib
from datetime import datetime


def create_hash(text: str):
  return hashlib.sha256(text.encode()).hexdigest()

# You can pass array of hashes in target
def compare_hash(current: str, target: str | list[str]) -> bool: 
  if type(target) is list:
    return current.lower() in [hash.lower() for hash in target]
  else:
    return current.lower() == target.lower()


# print(compare_hash('123', '123'))
# print(compare_hash('a1A', ['a1A']))
