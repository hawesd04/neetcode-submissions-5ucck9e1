class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            hash_set = set()
            for element in row:
                if element not in hash_set and element != ".":
                    hash_set.add(element)
                elif element != ".":
                    return False

        for col_idx in range(9):
            hash_set = set()
            for row in board:
                element = row[col_idx]
                if element not in hash_set and element != ".":
                    hash_set.add(element)
                elif element != ".": 
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                hash_set = set()
                subgrid = [row[j:j+3] for row in board[i:i+3]]
                for row in subgrid:
                    for element in row:
                        if element not in hash_set and element != ".":
                            hash_set.add(element)
                        elif element != ".":
                            return False

        return True