def generateParenthesis(self, n: int) -> List[str]:
    answer = []
    
    def generate(s, left, right):
        if len(s) == 2*n:
            answer.append(s)

        if left > 0:
            generate(s + '(', left-1, right)
        
        if right > 0 and right > left:
            generate(s + ')', left, right-1)

    generate("",n,n)
    
    return answer