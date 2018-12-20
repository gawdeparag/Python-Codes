def caesar(plainText):
    result = ""
    for pT in range(len(plainText)):
        cT = plainText[pT]

        if(cT.isupper()):
            result += chr((ord(cT) + 3-65) % 26 + 65)

        else:
            result += chr((ord(cT) + 3-97) % 26 + 97)

    return result

plainText = input("Enter your plaintext: ")
print("Cipher Text: " + caesar(plainText))