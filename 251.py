"""
Implement an iterator to flatten a 2d vector.

Example:

Input: 2d vector =
[
  [1,2],
  [3],
  [4,5,6]
]
Output: [1,2,3,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,2,3,4,5,6].
Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vector = vec2d
        self.row = 0
        self.nextNotEmpty()
        self.col = 0
        
    def nextNotEmpty(self):
        while self.row < len(self.vector) and len(self.vector[self.row]) == 0:
            self.row += 1
        return
            
    def next(self):
        """
        :rtype: int
        """
        ans = self.vector[self.row][self.col]
        self.col += 1
        if self.col >= len(self.vector[self.row]):
            self.col = 0
            self.row += 1
            self.nextNotEmpty()
        return ans
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.row < len(self.vector)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
