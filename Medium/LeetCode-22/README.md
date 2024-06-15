# Generate Parentheses

## Problem Statement
[Generate Parentheses Problem Description](https://leetcode.com/problems/generate-parentheses/description/)

## Explanation

### Algorithm:
1. Initialize an empty list answer to store valid combinations of parentheses.
2. Define a recursive helper function generate(s, left, right) to generate valid combinations of parentheses.
3. Base case: If the length of the string s is equal to 2*n, add s to the answer list.
4. Recursive cases:
    - If left is greater than 0, call generate(s + '(', left-1, right), decrementing left.
    - If right is greater than 0, right is greater than left, call generate(s + ')', left, right-1), decrementing right.
5. Call generate("", n, n) to start the recursion with n opening and n closing parentheses.
6. Return the answer list containing all valid combinations of parentheses.

### Time Complexity:
- The time complexity is O(4^n / sqrt(n)) due to the Catalan number of valid combinations of parentheses.

### Space Complexity:
- The space complexity is O(4^n / sqrt(n)) for storing all valid combinations of parentheses.