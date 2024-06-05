def checkUnique_01(string):
    n = len(string)
    
    for i in range(0, n):
        for j in range(i+1, n):
            if string[i] == string[j]:
                return False

    return True

def checkUnique_02(string):
    n = len(string)

    if n > 128:
        return False

    char_set = [None] * 128

    for i in range(n):
        val = ord(string[i])

        if(char_set[val]):
            return False
        
        char_set[val] = True
    
    return True

def logAnswer(flag):
    if flag:
        return "Unique"
    else:
        return "not Unique"


def chooseMethod(lang, string):
    match lang:
        case "1":
            print("This method use a loop to check, so the O(n) = n^2 \n")
            print("The string you entered is ", logAnswer(checkUnique_01(string)))
        case "2":
            print("This method create a char set of ASCII (remember to verify this info with the interviewer), so the O(n) = n \n")
            print("The string you entered is ", logAnswer(checkUnique_02(string)))
        case _:
            print("Please choose again!")



def main():
    #Note: Can clarify with the interviewer that the string is in ASCII or Unicode
    #In this case, I assume that it is in ASCII and has 128 unique characters

    print("Check if the characters in the string are all unique! \n")

    string = input("Enter the string to check: ")
    print("You entered: ", string)

    lang = input("Which method you want?: ")

    chooseMethod(lang, string)



if __name__ == '__main__':
    main()