# Reverse Integer

## Problem Statement
[Reverse Integer Problem Description](https://leetcode.com/problems/reverse-integer/description/)

## Explanation

### Algorithm:
1. Initialize a boolean variable flag to False.
2. If the input integer x is negative:
    - Set flag to True.
    - Convert x to its positive equivalent by multiplying it by -1.
3. Initialize an integer variable ans to 0 to store the reversed number.
4. While x is greater than 0:
    - Update ans by multiplying it by 10 and adding the last digit of x (x % 10).
    - Remove the last digit from x by performing integer division by 10 (x = x // 10).
5. After exiting the loop, check if ans exceeds the 32-bit signed integer range (2^31 - 1):
    - If it does, return 0.
6. If flag is True, return ans multiplied by -1 to restore the negative sign.
7. Otherwise, return ans.

### Time Complexity:
- The time complexity is O(d), where d is the number of digits in the input integer x. This is because the algorithm processes each digit exactly once in the while loop.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a constant amount of extra space for variables and does not depend on the input size.