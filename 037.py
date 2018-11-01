"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
    def solve(self, board):
        row, col = self.find_empty(board)
        if row == -1:
            return True
        
        for num in range(1,10):
            if self.valid(board, row, col, str(num)):
                board[row][col] = str(num)
                
                if self.solve(board): 
                    return True
                board[row][col] = '.'
                    
                
        return False
        
        
        
    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': return (i,j)
        return (-1,-1)
                
    def digit_in_row(self, board, row, col, num):
        for c in range(9):
            if board[row][c] == num: return True
        return False
    
    def digit_in_col(self, board, row, col, num):
        for r in range(9):
            if board[r][col] == num: return True
        return False
    
    def digit_in_box(self, board, row, col, num):
        for i in range((row/3) * 3, (row/3)*3+3):
            for j in range((col/3)*3, (col/3)*3+3):
                if board[i][j] == num: return True
        return False
    
    def valid(self, board, row, col, num):
        return not self.digit_in_row(board, row, col, num) and not self.digit_in_col(board, row, col, num) and not self.digit_in_box(board, row, col, num)
    
        
