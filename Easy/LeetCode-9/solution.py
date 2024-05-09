def isPalindrome(self, x: int) -> bool:
    str_x= str(x)
    y = str_x[::-1]
    print (y)
    
    if str_x == y:
        return True
    else:
        return False