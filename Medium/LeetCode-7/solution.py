def reverse(self, x: int) -> int:
    flag = False

    if x<0:
        flag = True
        x = x*-1
    
    ans = 0
    while x > 0:
        ans = ans*10 + (x%10)
        x = x//10

    if ans > 2 ** 31 -1:
        return 0
    
    if flag:
        return ans * -1
    else:
        return ans