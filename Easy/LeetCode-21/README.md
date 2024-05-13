# Merge Two Sorted Lists

## Problem Statement
[Merge Two Sorted Lists Problem Description](https://leetcode.com/problems/merge-two-sorted-lists/description/)

## Explanation
### Algorithm:
1. Create a new linked list mergeList to store the merged list, and initialize a pointer head to the beginning of mergeList.
2. Iterate through both list1 and list2 simultaneously using a while loop until either of them becomes None.
In3. side the loop:
    - If list1 is None, append the value of the current node in list2 to mergeList, and move list2 to the next node.
    - If list2 is None, append the value of the current node in list1 to mergeList, and move list1 to the next node.
    - If both list1 and list2 are not None, compare the values of the current nodes in list1 and list2. Append the smaller value to mergeList, and move the corresponding list pointer to the next node.
4. After the loop, if there are remaining nodes in list1 or list2, append them to mergeList.
5. Return the next node of head (skipping the dummy node), which is the head of the merged list.

### Time Complexity:
- The algorithm iterates through each node in list1 and list2 exactly once, resulting in a time complexity of O(m + n), where m and n are the lengths of list1 and list2 respectively.

### Space Complexity:
- The space complexity is O(1) as the algorithm uses a constant amount of extra space for variables and does not depend on the input size.