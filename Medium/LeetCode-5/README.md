# Longest Palindromic Substring

## Problem Statement
[Longest Palindromic Substring Problem Description](https://leetcode.com/problems/longest-palindromic-substring/description/)

## Explanation

### Algorithm:
1. Define a helper function check(s) that takes a string s and returns True if s is a palindrome, False otherwise.
2. If the input string s has length 1, return s as it is already a palindrome.
3. Initialize variables l (length of longest palindrome found so far) to 1 and output (longest palindrome found so far) to the first character of s.
4. Iterate over all possible substrings of s using two nested loops (indices i and j).
5. For each pair of indices i and j, check if the substring s[i:j+1] is a palindrome using the check function.
6. If the substring is a palindrome and its length is greater than l, update output and l to the current substring and its length respectively.
7. After iterating over all substrings, return output as the longest palindrome found.

### Time Complexity:
- The check function takes O(n) time, where n is the length of the input string s.
- The nested loops iterate over all possible substrings of s, resulting in a time complexity of O(n^3) to generate all substrings and check if they are palindromes.
- Therefore, the overall time complexity is O(n^3).

### Space Complexity:
- The space complexity is O(1) for the check function as it uses a constant amount of space.
- The space complexity of the algorithm is dominated by the space required to store the output string output, which can be at most the length of s. Therefore, the space complexity is O(n) where n is the length of s.