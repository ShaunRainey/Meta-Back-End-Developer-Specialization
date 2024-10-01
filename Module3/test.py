def isPalindrome(string):
    i= len(string) -1
    newString = ''
    while i>= 0:
        newString += string[i].upper()
        i -= 1
    if string.upper() == newString:
        print(True)
        return True
    else:
        print(False)
        return False

isPalindrome('TacOct')