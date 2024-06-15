def isValidSudoku(self, board: List[List[str]]) -> bool:
    n = 9

    row = [set() for _ in range(n)]
    col = [set() for _ in range(n)]
    box = [set() for _ in range(n)]

    for r in range(n):
        for c in range(n):
            val = board[r][c]

            if val == '.':
                continue

            if val in row[r]:
                return False
            row[r].add(val)

            if val in col[c]:
                return False
            col[c].add(val)

            b = int(r/3)*3 + int(c/3)

            if val in box[b]:
                return False
            box[b].add(val)
    return True