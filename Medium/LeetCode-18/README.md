# 4Sum

## Problem Statement
[4Sum Problem Description](https://leetcode.com/problems/4sum/description/)

## Explanation

### Algorithm:
1. Define a helper function threeSum(nums, target, a) to find all unique triplets in nums that sum up to target and include nums[a].
2. Within threeSum, use two pointers technique to find triplets (nums[a], nums[b], nums[c], nums[d]) where b, c, and d are indices after a.
    - If the current sum is less than target, increment c.
    - If the current sum is greater than target, decrement d.
    - If the current sum is equal to target, add the quadruplet to the output list and increment c and decrement d while skipping duplicates.
3. Sort the input list nums.
4. Iterate over the indices a from 0 to n - 4 (where n is the length of nums):
    - Skip duplicates by checking if a is at the beginning or if the current element is different from the previous element.
    - Call threeSum(nums, target, a) to find triplets using elements after a.
5. Return the output list containing all unique quadruplets.

### Time Complexity:
- Sorting the list takes O(n * log(n)) time.
- The main loop iterates through each element once, resulting in a time complexity of O(n) for the loop.
- Inside the threeSum function, the two pointers technique takes O(n) time.
- Therefore, the overall time complexity is O(n^3) due to the nested loops and the sorting dominating the time complexity.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a constant amount of extra space for variables and does not depend on the input size.