"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = []
        if not grid:
            return 0
        
        numRows = len(grid)
        numCols = len(grid[0])
        for i in xrange(numRows):
            visited.append([0]*len(grid[0]))
        
        islands = 0
        
        def getAdjacent(row, col):
            ans = []
            #print "getAdjacent: ", row, col
            #check up
            if row - 1 >= 0 and visited[row-1][col] == 0:
                ans.append((row-1,col))
                visited[row-1][col] = 1
            #check right
            if col + 1 < numCols and visited[row][col+1] == 0:
                ans.append((row, col+1))
                visited[row][col+1] = 1
            #check down
            if row + 1 < numRows and visited[row+1][col] == 0:
                ans.append((row+1, col))
                visited[row+1][col] = 1
            #check left
            if col - 1 >= 0 and visited[row][col-1] == 0:
                ans.append((row, col-1))
                visited[row][col-1] = 1
            #print ans
            return ans
        
        def getIsland(row, col):
            q = collections.deque()
            for g in getAdjacent(row, col):
                q.append(g)
            while q:
                r, c = q.popleft()
                #print "checking: ",r,c, grid[r][c]
                if grid[r][c] == "1":
                    for g in getAdjacent(r,c):
                        #print "appending ", g
                        q.append(g)
                
        
        for i in range(numRows):
            for j in range(numCols):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    if grid[i][j] == "1":
                        islands += 1
                        getIsland(i,j)
                        #print visited
        #print visited
        return islands
