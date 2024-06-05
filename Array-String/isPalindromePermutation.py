# def isPalindrome(string):
#     string = ''.join(string.split())
    
#     n = len(string)

#     for i in range(int(n/2)):
#         if string[i] != string[n-i-1]:
#             return False
    
#     return True

#Note: check if it is a palindrome from the char counts, not when it is generated

#solution 1
def isPalindromePermutation(string):
    #remove all spaces
    string = ''.join(string.split())

    #assume it is in ASCII
    n = len(string)

    if n>128:   
        return False
    
    char_count = [0] * 128

    for i in range(n):
        val = ord(string[i])
        char_count[val]+=1

    one_odd = False
    for x in char_count:
        if x % 2 != 0:
            if not one_odd:
                one_odd = True
            else:
                return False
    
    return True

#solution 1 but modifed when it removed all non-letter chars and are case insensitive
def isPalindromePermutation_modified(s: str) -> bool:
    table = buildCharFrequencyTable(s)
    return checkOddTable(table)

def getCharNumber(char: str) -> int:
    a = ord('a')
    z = ord('z')
    val = ord(char.lower())

    if val>=a and val<=z:
        return val-a
    
    return -1

def buildCharFrequencyTable(s: str) -> list:
    n = int(ord('z') - ord('a') + 1)
    table = [0] * n

    for char in s:
        val = getCharNumber(char)
        if val != -1:
            table[val] +=1

    return table

def checkOddTable(table: list) -> bool:
    one_odd = False
    for x in table:
        if x % 2 != 0:
            if one_odd:
                return False
            one_odd = True
    
    return True 
    



def main():
    string = input('Enter the string: ')
    #print(isPalindromePermutation(string))
    print(isPalindromePermutation_modified(string))


if __name__ == "__main__":
    main()
