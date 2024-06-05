def isPermutation(string_1, string_2):
    #assume this string is in ASCII and has 128 chars
    n = len(string_1)
    if n>128:
        return False
    
    if n != len(string_2):
        return False
    
    char_set_1 = [0] * 128
    char_set_2 = [0] * 128

    for i in range(n):
        val_1 = ord(string_1[i])
        val_2 = ord(string_2[i])

        char_set_1[val_1] += 1
        char_set_2[val_2] += 1


    if char_set_1 != char_set_2:
        return False
    
    
    return True

def main():
    print("Check if the string is permutation or not \n")

    print("Enter 2 strings want to test!")

    string_1 = input("First string: ")
    string_2 = input("Second string: ")

    print(isPermutation(string_1, string_2))

if __name__ == "__main__":
    main()

#First attemp with boolean charset but not inclusive for the duplicated chars
# => should count the chars instead of only count once by put True or False

#Solution #1: Sort the strings.
#Solution #2: Check if the two strings have identical character counts.