def longestPalindrome(self, s: str) -> str:
    def check(s):
        rev_s = s[::-1]
        if rev_s == s:
            return True
        else:
            return False
    
    if len(s) == 1:
        return s
    
    l = 1
    output = s[0]

    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            check_s = s[i:j+1]  
            flag = check(check_s)

            if flag and  len(check_s) > l:
                output = check_s
                l = len(check_s)      
    
    return output