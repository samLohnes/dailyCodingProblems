

def isPalindrome(x):

    string = str(x)

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    
    return True


assert isPalindrome(121) == True
assert isPalindrome(-121) == False
assert isPalindrome(10) == False
assert isPalindrome(10101) == True