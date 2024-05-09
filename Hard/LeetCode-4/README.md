# Median of Two Sorted Arrays

## Problem Statement
[Median of Two Sorted Arrays Problem Description](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

## Explanation

### Algorithm:
1. Define a helper function calculateMedian that takes a sorted array as input and returns the median of the array.
2. If either nums1 or nums2 is empty, return the median of the non-empty array using the calculateMedian function.
3. Merge nums1 and nums2 into a single sorted array by concatenating them and sorting the result.
4. Return the median of the merged array using the calculateMedian function.

### Time Complexity:
- Merging nums1 and nums2 into a single sorted array using concatenation and sorting takes O((m+n)log(m+n)) time, where m and n are the lengths of nums1 and nums2 respectively.
- Calculating the median using the calculateMedian function takes O(1) time.
- Therefore, the overall time complexity is dominated by the sorting step, resulting in O((m+n)log(m+n)) time complexity.

### Space Complexity:
- The space complexity is O(m+n) to store the merged array, where m and n are the lengths of nums1 and nums2 respectively.
- The space complexity of the calculateMedian function is O(1) as it only uses a constant amount of space for variables.
- Therefore, the overall space complexity is O(m+n).