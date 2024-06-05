# - Replacement: Consider two strings, such as bale and pale, that are one replacement away. Yes, that
# does mean that you could replace a character in bale to make pale. But more precisely, it means that
# they are different only in one place.

# - Insertion: The strings apple and aple are one insertion away. This means that if you compared the
# strings, they would be identical-except for a shift at some point in the strings.

# - Removal: The strings apple and aple are also one removal away, since removal is just the inverse of
# insertion.

def main():
    print("Check if the string is one edit or not!")

    string = input('Enter the original string: ')
    e_string = input('Enter the edited string: ')
    print(checkOneEdit(string, e_string))

def checkOneEdit(string_1: str, string_2: str) -> bool:
    n1 = len(string_1)
    n2 = len(string_2)

    if n1 == n2:
        return oneEditReplace(string_1, string_2)
    else:
        if n1 -1 == n2:
            return oneEditInsertion(string_1, string_2)
        else:
            if n1 == n2 -1:
                return oneEditInsertion(string_2, string_1)
            
    return False

def oneEditReplace(string_01: str, string_02: str) -> bool:
    oneDiferrence = False

    for char_1, char_2 in zip(string_01, string_02):
        if char_1 != char_2:
            if oneDiferrence:
               return False
            oneDiferrence = True

    return True   
  
def oneEditInsertion(string_01: str, string_02: str) -> bool:
    index_1 = 0
    index_2 = 0

    while index_2 < len(string_02) and index_1 < len(string_01):
        if string_01[index_1] != string_02[index_2]:
            if index_1 != index_2:
                return False
            else:
                index_2 += 1
        else:
            index_1 +=1
            index_2 +=1

    return True   

if __name__ == "__main__":
    main()