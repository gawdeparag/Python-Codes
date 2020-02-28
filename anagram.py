def isAnagram(string1, string2):
    string1 = string1.replace(" ", "").join("")
    string2 = string2.replace(" ", "").join("")

    anagram = 0
    notAnagram = 0

    if(string1 != string2):
        return 0
    else:
        length1 = len(string1)
        length2 = len(string2)

        string1 = sorted(string1)
        string2 = sorted(string2)

        for i in range(0, length1):
            if(string1[i] == string2[i]):
                anagram += 1
            else:
                notAnagram += 1

        if anagram == length1:
            return 1
        else:
            return 0

if __name__ == "__main__":
    string1 = input("Enter the first string: ").strip().lower()
    string2 = input("Enter the second string: ").strip().lower()
    if string1 == string2:
        print("Both are not Anagrams")
    else:        
        if isAnagram(string1, string2) == 1:
            print("Both are Anagrams")
        else:
            print("Both are not Anagram")
