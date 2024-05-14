# Remove Element

## Problem Statement
[Remove Element Problem Description](https://leetcode.com/problems/remove-element/description/)

## Explanation
### Algorithm:
1. Initialize an index i to 0.
2. Iterate over the list nums using while loop until i reaches the length of nums:
- If nums[i] is equal to val, remove nums[i] from nums using nums.pop(i).
- If nums[i] is not equal to val, increment i to move to the next element.
3. After iterating through all elements, return the length of nums.

### Time Complexity:
- The algorithm iterates through each element in the nums list at most once, resulting in a time complexity of O(n), where n is the length of nums.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a constant amount of extra space for variables and does not depend on the input size.