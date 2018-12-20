p = int(input("Enter the Prime Modulus: "))
g = int(input("Enter the Generator: "))

a = int(input("Enter the private key of Alice: "))
b = int(input("Enter the private key of Bob: "))

x = (g**a)%p
y = (g**b)%p

keyA = (y**a)%p
keyB = (x**b)%p

if(keyA == keyB):
    print ("The shared secret key is: ", keyA)
    print("Transaction successful!")
else:
    print("Transaction failed!")