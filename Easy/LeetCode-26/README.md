# Remove Duplicates from Sorted Array

## Problem Statement
[Remove Duplicates from Sorted Array Problem Description](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Explanation
### Algorithm:
1. Initialize an empty dictionary dic to store unique elements.
2. Initialize a counter ctr to count unique elements.
3. Iterate over the list nums using an index i:
- If nums[i] is already in dic, remove nums[i] from nums using nums.pop(i) to eliminate duplicates.
- If nums[i] is not in dic, add nums[i] to dic, increment ctr, and move to the next element (i+=1).
4. After iterating through all elements, return the value of ctr as the number of unique elements in nums.

### Time Complexity:
- The algorithm iterates through each element in the nums list at most once, resulting in a time complexity of O(n), where n is the length of nums.

### Space Complexity:
- The space complexity is O(n) in the worst case scenario where all elements in nums are unique, and dic contains all elements of nums.