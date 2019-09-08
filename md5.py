import hashlib

message = input("Enter your message here: ")
result = hashlib.md5(message.encode())

# printing the equivalent byte value.
print("The byte equivalent of hash is : ")
print(result.digest())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ")
print(result.hexdigest())
