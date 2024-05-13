def isValid(self, s: str) -> bool:
    mapping = {')':'(','}':'{', ']':'['}

    stack = []

    for ch in s:
        if ch in {'(', '{', '['}:
            stack.append(ch)
        else:
            if len(stack) != 0 and mapping[ch] == stack[-1]:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    else:
        return True