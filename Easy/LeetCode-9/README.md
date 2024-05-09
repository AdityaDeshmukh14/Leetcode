# Palindrome Number

## Problem Statement
[Palindrome Number Problem Description](https://leetcode.com/problems/palindrome-number/description/)

## Explanation

### Algorithm:
1. Convert the integer x to a string str_x.
2. Reverse the string str_x to obtain y.
3. If the reversed string y is equal to the original string str_x, return True, indicating that the integer x is a palindrome. Otherwise, return False.

### Time Complexity:
- Converting an integer to a string (str(x)) takes O(log(x)) time, where log(x) is the number of digits in x.
- Reversing a string (str_x[::-1]) takes O(n) time, where n is the length of the string.
- Comparing two strings (str_x == y) takes O(n) time, where n is the length of the string.
- Therefore, the overall time complexity is O(log(x) + n).

### Space Complexity:
- Converting an integer to a string (str(x)) requires O(log(x)) additional space to store the string representation of x.
- Reversing the string (y = str_x[::-1]) creates a new string y, requiring O(n) additional space, where n is the length of the string.
- Therefore, the overall space complexity is O(log(x) + n).