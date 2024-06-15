# Search in Rotated Sorted Array

## Problem Statement
[Search in Rotated Sorted Array Problem Description](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

## Explanation

### Algorithm:
1. Initialize two pointers, left and right, to the start and end of the nums list respectively.
2. Use a while loop to iterate while left is less than or equal to right:
    - Calculate the middle index mid as left + (right - left) // 2.
    - Check if nums[mid] is equal to target. If it is, return mid.
    - Check if the left half of the array is sorted (nums[left] <= nums[mid]):
        - If target is in the left half (nums[left] <= target < nums[mid]), update right to mid - 1.
        - Otherwise, update left to mid + 1.
    - If the right half of the array is sorted (nums[mid] < nums[right]):
        - If target is in the right half (nums[mid] < target <= nums[right]), update left to mid + 1.
        - Otherwise, update right to mid - 1.
3. If the loop completes without finding the target, return -1.

### Time Complexity:
- The time complexity is O(log n) where n is the length of nums, as the array is divided in half at each step in the binary search.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a constant amount of extra space regardless of the input size.