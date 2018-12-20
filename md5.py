import hashlib

result = hashlib.md5(b'AttackBeijing')

# printing the equivalent byte value.
print("The byte equivalent of hash is : ")
print(result.digest())
