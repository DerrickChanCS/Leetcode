"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        from collections import deque
        queue = deque()
        queue.append(1)
        for _ in xrange(n-1):
            num = queue[0]
            count = 0
            temp = deque()
            while queue:
                while queue and queue[0] == num:
                    count += 1
                    queue.popleft()
                temp.append(count)
                temp.append(num)
                if queue:
                    num = queue[0]
                    count = 0
            queue = temp
        ans = ""
        for c in queue:
            ans += str(c)
        return ans
                    
