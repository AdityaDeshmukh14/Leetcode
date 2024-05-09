# Add Two Numbers

## Problem Statement
[Add Two Numbers Problem Description](https://leetcode.com/problems/add-two-numbers/description/)

## Explanation

### Algorithm:
1. Initialize carry to 0.
2. Create a dummy node sumList to store the sum of the two linked lists.
3. Initialize a pointer l3 to sumList for iterating and constructing the result linked list.
4. Iterate through both linked lists l1 and l2 until either of them becomes None.
    - Calculate the sum of the current nodes' values along with the carry.
    - Update the carry for the next iteration.
    - Create a new node with the sum value and append it to sumList.
    - Move to the next nodes in l1 and l2.
5. If there is a remaining carry after iterating through both linked lists, append a new node with the carry to sumList.
6. Return the next node of sumList (skipping the dummy node), which is the head of the resulting sum linked list.

### Time Complexity:
- The algorithm traverses both linked lists l1 and l2 at most once, resulting in a time complexity of O(max(m, n)), where m and n are the lengths of l1 and l2 respectively.

### Space Complexity:
- The space complexity is O(max(m, n)), where m and n are the lengths of l1 and l2 respectively. This is because the algorithm creates a new linked list to store the sum, which can be at most the length of the longer of the two input linked lists.