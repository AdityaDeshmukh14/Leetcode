# Longest Common Prefix

## Problem Statement
[Longest Common Prefix Problem Description](https://leetcode.com/problems/longest-common-prefix/description/)

## Explanation

### Algorithm:
1. Sort the input list of strings strs lexicographically.
2. Get the first and last string from the sorted list.
3. Iterate through the characters of the first and last string simultaneously up to the length of the shorter string.
4. If the characters at the same index are equal, append the character to the answer.
5. If the characters are not equal, return the current answer.
6. After the loop, return the final answer.

## Time Complexity:
- Sorting the list of strings takes O(n * m * log(m)) time, where n is the number of strings in the list and m is the average length of the strings.
- The iteration through the characters of the first and last string takes O(m) time.
- Therefore, the overall time complexity is O(n * m * log(m)).

### Space Complexity:
- The space complexity is O(1) as the algorithm uses only a constant amount of extra space for variables and does not depend on the input size.