"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dynamic programming lul
        # Time: O(mn)
        # Space: O(mn)
        # This solution minimizes the path to any particular
        #   cell in the grid
        
        # First generate the shortest path if you only go right
        # The only possible path for this configuration is if you
        #   move right only
        numRows = len(grid)
        numCols = len(grid[0])
        for col in xrange(1, numCols):
            grid[0][col] += grid[0][col-1]
        
        # Generate the shortest path if you only go down
        for row in xrange(1, numRows):
            grid[row][0] += grid[row-1][0]
            
        # Generate the shortest path for any particular cell
        for row in xrange(1, numRows):
            for col in xrange(1, numCols):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
        
        # Return the shortest path to the last cell
        return grid[numRows-1][numCols-1]
