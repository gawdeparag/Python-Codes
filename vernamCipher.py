def vernam(plainText, key):
    result = ""
    ptr = 0
    for pT in plainText:
        result += chr(ord(pT) ^ ord(key[ptr]))
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return result

while True:
    plainText = input("Enter your Plain Text: ")
    key = "encryptionusingpython"
    result = vernam(plainText, key)
    print(result)