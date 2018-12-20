def vernam(plainText):
    result = ""
    key = "encryptionusingpython"
    ptr = 0
    for pT in plainText:
        result += chr(ord(pT) ^ ord(key[ptr]))
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return result

def caesar(plainText):
    result = ""
    for pT in range(len(plainText)):
        cT = plainText[pT]

        if(cT.isupper()):
            result += chr((ord(cT) + 3-65) % 26 + 65)

        else:
            result += chr((ord(cT) + 3-97) % 26 + 97)

    return result

def product(plainText):
    caesarText = caesar(plainText)
    vernamText = vernam(caesarText)

    return vernamText

plainText = input("Enter your Plain Text: ")
cipherText = product(plainText)

print(cipherText)