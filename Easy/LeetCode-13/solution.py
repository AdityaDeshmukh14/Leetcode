def romanToInt(self, s: str) -> int:
    rev_s = s[::-1]
    num = 0
    
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = value[rev_s[0]]

    for ch in rev_s:
        if value[ch] < prev:
            num -= value[ch]
        else:
            num += value[ch]
        prev = value[ch]

    return num