def lengthOfLongestSubstring(self, s: str) -> int:
    used = {}
    maxLength = 0 
    start = 0

    for index, ch in enumerate(s):
        if (ch in used and start <= used[ch]):
            start = used[ch]+1
        else:
            maxLength = max(maxLength, index - start + 1)
        used[ch] = index    

    return maxLength