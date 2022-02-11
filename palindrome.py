def check_palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    if str == str[::-1]:
        return True
    else:
        return False
    
print(check_palindrome("a"))
print(check_palindrome("michael"))
print(check_palindrome("hannah"))
print(check_palindrome("madam"))
print(check_palindrome("seats"))
