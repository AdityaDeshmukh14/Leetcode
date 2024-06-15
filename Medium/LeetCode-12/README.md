# Integer to Roman

## Problem Statement
[Integer to Roman Problem Description](https://leetcode.com/problems/integer-to-roman/description/)

## Explanation

### Algorithm:
1. Initialize a dictionary romanDict that maps integer values to their corresponding Roman numeral symbols.
2. Initialize an empty string roman to build the resulting Roman numeral.
3. Iterate over each key in romanDict:
    - For each key, calculate the number of times the key can be divided into the current value of num using integer division (num // key).
    - Append the corresponding Roman numeral symbol (romanDict[key]) to the roman string this number of times.
    - Update num to the remainder after division (num % key).
4. Return the roman string as the final result.

### Time Complexity:
- The time complexity is O(1) because the number of Roman numeral symbols is fixed (13 in total) and does not depend on the input size. The algorithm iterates over this fixed number of symbols in constant time.

### Space Complexity:
- The space complexity is O(1) because the amount of extra space used by the algorithm does not depend on the input size. The dictionary and the resulting string roman use a fixed amount of space.