# Valid Sudoku

## Problem Statement
[Valid Sudoku Problem Description](https://leetcode.com/problems/valid-sudoku/description/)

## Explanation

### Algorithm:
1. Initialize three lists of sets, row, col, and box, each of length 9, to keep track of the numbers seen in each row, column, and 3x3 sub-box respectively.
2. Iterate over each cell in the board using two nested loops, where r is the row index and c is the column index:
    - Get the value val at board[r][c].
    - If val is '.', continue to the next cell.
    - Check if val is already in the set for the current row row[r]. If it is, return False.
    - Add val to the set for the current row row[r].
    - Check if val is already in the set for the current column col[c]. If it is, return False.
    - Add val to the set for the current column col[c].
    - Calculate the index of the 3x3 sub-box as b = (r // 3) * 3 + (c // 3).
    - Check if val is already in the set for the current 3x3 sub-box box[b]. If it is, return False.
    - Add val to the set for the current 3x3 sub-box box[b].
3. If no duplicates are found, return True.

### Time Complexity:
- The time complexity is O(n^2), where n is the length of the board (n = 9 in this case). This is because each cell is visited once.

### Space Complexity:
- The space complexity is O(n), as three lists of sets of length 9 are used to store the seen values for rows, columns, and sub-boxes. 
- This is constant space relative to the size of the input, as n = 9 is fixed for a standard Sudoku board.