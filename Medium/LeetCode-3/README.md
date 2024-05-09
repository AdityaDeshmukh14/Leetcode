# Longest Substring Without Repeating Characters

## Problem Statement
[Longest Substring Without Repeating Characters Problem Description](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

## Explanation

### Algorithm:
1. Initialize an empty dictionary used to keep track of the most recent index of each character.
2. Initialize maxLength to 0 to store the length of the longest substring without repeating characters.
3. Initialize start to 0 to keep track of the start index of the current substring.
4. Iterate over each character ch in the input string s using enumerate to track the index.
5. If ch is already in used and its index is greater than or equal to start, update start to the next index after the last occurrence of ch.
6. Update maxLength to the maximum of its current value and the length of the current substring (index - start + 1).
7. Update the index of ch in used to the current index.
8. Return maxLength as the length of the longest substring without repeating characters.

### Time Complexity:
- The algorithm iterates through each character in the input string s once, resulting in a time complexity of O(n), where n is the length of s.

### Space Complexity:
- The space complexity is O(min(m, n)), where m is the size of the character set (number of unique characters) and n is the length of the input string s. 
- In the worst case, all characters in s are unique, so m is equal to n, and the space complexity becomes O(n). The space is used to store the indices of characters in the used dictionary.