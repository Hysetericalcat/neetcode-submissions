class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row_check():
            for row in board:
                row = [x for x in row if x != "."]
                if len(set(row))!= len(row):
                    return False
            return True

        def col_check():
            for i in range(0,9):
                arr = []
                for j in range(0,9):
                   arr.append(board[j][i])
                arr = [x for x in arr if x != "."]
                if len(set(arr))!=len(arr):
                    return False
            return True

        def matrix_check():
            for start_i in range(0, 9, 3):      
                for start_j in range(0, 9, 3):  
                    arr = []

                    for i in range(start_i, start_i + 3):
                       for j in range(start_j, start_j + 3):
                           arr.append(board[i][j])
                    arr = [x for x in arr if x != "."]
                    if len(arr) != len(set(arr)):
                         return False
            return True
           
    
        if row_check() and col_check() and matrix_check():
            return True
        return False          
            

                    

                
                    
