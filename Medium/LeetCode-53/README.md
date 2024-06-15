# Maximum Subarray

## Problem Statement
[Maximum Subarray Problem Description](https://leetcode.com/problems/maximum-subarray/description/)

## Explanation

### Algorithm:
1. Initialize maxSum to negative infinity to store the maximum subarray sum found so far.
2. Initialize currentSum to 0 to keep track of the current subarray sum.
3. Iterate through each number num in the list nums:
    - Add num to currentSum.
    - If currentSum is greater than maxSum, update maxSum to currentSum.
    - If currentSum is less than 0, reset currentSum to 0.
4. Return maxSum as the maximum subarray sum.

### Time Complexity:
- The time complexity is O(n), where n is the length of the nums list. This is because we iterate through the list once.

### Space Complexity:
- The space complexity is O(1), as the algorithm uses a constant amount of extra space regardless of the input size.