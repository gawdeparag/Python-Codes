def voconst(word):
	v = 0
	c = 0
	for letter in word:
		if (letter == 'a' or letter == 'i' or letter == 'o' or letter == 'e' or letter == 'u'):
			v = v + 1
		elif (letter == 'A' or letter == 'I' or letter == 'O' or letter == 'E' or letter == 'U'):
			v = v + 1
		else:
			c = c + 1

	print("Number of vowels: ", v)
	print("Number of constants: ", c)

word = input("Enter a word: ")
voconst(word)