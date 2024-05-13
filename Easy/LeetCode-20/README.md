# Valid Parentheses

## Problem Statement
[Valid Parentheses Problem Description](https://leetcode.com/problems/valid-parentheses/description/)

## Explanation
### Algorithm:
1. Initialize a dictionary mapping to map closing brackets to their corresponding opening brackets.
2. Initialize an empty stack stack to store opening brackets.
3. Iterate through each character ch in the input string s.
    - If ch is an opening bracket ('(', '{', '['), push it onto the stack.
    - If ch is a closing bracket (')', '}', ']'), check if the stack is not empty and the top element of the stack is the corresponding opening bracket for ch. If so, pop the top element from the stack. Otherwise, return False.
4. After iterating through all characters, if the stack is not empty, return False (there are unmatched opening brackets). Otherwise, return True.

### Time Complexity:
- The algorithm iterates through each character in the input string s, resulting in a time complexity of O(n), where n is the length of s.

### Space Complexity:
- The space complexity is O(n), where n is the length of the input string s. This is because the stack can potentially store all opening brackets in the worst case scenario, which is when s consists entirely of opening brackets.