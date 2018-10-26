"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # bottom up approach
        rows = len(triangle)
        path = []
        for i in xrange(rows):
            path.append(triangle[rows-1][i])
            
        for i in xrange(rows-2, -1, -1):
            for k in xrange(0, i+1):
                path[k] = min(path[k], path[k+1]) + triangle[i][k]
            #print path
        """        
        for i in xrange(rows-2, -1, -1):
            for k in xrange(0, i+1):
                triangle[i][k] = min(triangle[i+1][k], triangle[i+1][k+1]) + triangle[i][k]
        """
        return path[0]
            
