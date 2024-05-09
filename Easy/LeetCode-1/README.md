# Two Sum

## Problem Statement
[Two Sum Problem Description](https://leetcode.com/problems/two-sum/description/)

## Explanation

### Algorithm:
1. Initialize an empty dictionary visited to store the indices of visited numbers.
2. Iterate over the nums list using enumerate to track both the index and the value.
3. For each number val in nums, calculate the complement rem by subtracting val from the target.
4. If the complement rem is already in visited, return the indices of the current number val and the complement rem.
5. Otherwise, add the current number val to visited with its index as the value.
6. If no two numbers sum up to the target, return an empty list.

### Time Complexity:
- The time complexity of this algorithm is O(n), where n is the number of elements in the nums list. The for loop iterates through each element once, and the dictionary lookup for rem in visited is an O(1) operation on average.

### Space Complexity:
- The space complexity is O(n) in the worst-case scenario. This is because the visited dictionary can store up to n key-value pairs if each number in the nums list is distinct.
