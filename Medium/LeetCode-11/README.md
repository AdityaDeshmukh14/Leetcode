# Container With Most Water

## Problem Statement
[Container With Most Water Problem Description](https://leetcode.com/problems/container-with-most-water/description/)

## Explanation

### Algorithm:
1. Initialize maxArea to 0 to keep track of the maximum area found.
2. Initialize two pointers, i at the beginning (0) and j at the end (len(height) - 1) of the height list.
3. Use a while loop to iterate as long as i is less than j:
    - Calculate the gap between the two pointers: gap = j - i.
    - Find the minimum height between height[i] and height[j]: minHeight = min(height[i], height[j]).
    - Calculate the current area as the product of gap and minHeight: area = gap * minHeight.
    - Update maxArea if the current area is greater than maxArea.
    - If height[i] is less than height[j], increment i by 1 to move the left pointer inward.
    - Otherwise, decrement j by 1 to move the right pointer inward.
4. After the loop, return maxArea.

### Time Complexity:
- The time complexity is O(n), where n is the length of the height list. This is because each element is processed at most once as the two pointers move inward.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a constant amount of extra space for variables and does not depend on the input size.