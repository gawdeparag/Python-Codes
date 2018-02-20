def voconst(word):
    v = 0
    c = 0
    for letter in word:
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            v = v + 1
        elif letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            v = v + 1
        else:
            c = c + 1

    print("Number of vowels: ", v)
    print("Number of constants: ", c)

word = input("Enter a string: ")
voconst(word)