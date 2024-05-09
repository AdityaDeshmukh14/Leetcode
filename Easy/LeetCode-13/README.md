# Roman to Integer

## Problem Statement
[Roman to Integer Problem Description] (https://leetcode.com/problems/roman-to-integer/description/)

## Explaination

### Algorithm:
1. Reverse the input Roman numeral string.
2. Initialize num to 0 and prev to the value of the rightmost character in the reversed string.
3. Iterate over each character ch in the reversed string.
    - If value[ch] is less than prev, subtract value[ch] from num.
    - Otherwise, add value[ch] to num.
    - Update prev to value[ch].
4. Return num as the result.

### Time Complexity:
Reversing the input string takes O(n) time, where n is the length of the input string. The loop iterates through each character in the reversed string, which also takes O(n) time.
<br>
Overall, the time complexity is O(n).

### Space Complexity:
The space complexity is O(1) because the algorithm uses a constant amount of extra space for the value dictionary, num, prev, and the loop variables. The space required does not scale with the size of the input.