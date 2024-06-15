# 3Sum

## Problem Statement
[3Sum Problem Description](https://leetcode.com/problems/3sum/description/)

## Explanation

### Algorithm:
1. Sort the input list nums.
2. Initialize an empty list output to store the triplets that sum to zero.
3. Iterate over the sorted list nums from index 0 to n - 2 (where n is the length of nums):
    - If the current element is the same as the previous element (to avoid duplicates), move to the next element.
    - Initialize two pointers j and k at indices i + 1 and n - 1 respectively.
    - While j is less than k:
    - Calculate the sum of the current triplet (nums[i], nums[j], nums[k]).
    - If the sum is less than zero, increment j.
    - If the sum is greater than zero, decrement k.
    - If the sum is zero, add the triplet to output.
    - Move j to the next different element to skip duplicates.
    - Move k to the previous different element to skip duplicates.
4. Return output.

### Time Complexity:
- Sorting the list takes O(n * log(n)) time.
- The main loop iterates through each element once and the nested while loop traverses each element once in each direction, resulting in a total time complexity of O(n^2).
- Therefore, the overall time complexity is O(n^2) due to the nested loops dominating the sorting.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a constant amount of extra space for variables and does not depend on the input size.