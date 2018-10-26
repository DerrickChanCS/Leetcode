"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        # Recursive solution. 
        # Optimize by memoization
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        """
        """
        # Can further optimize by only storing the previous two values
        steps = [-1] * (n+1)
        if n >= 3:
            steps[0] = 1
            steps[1] = 1
            steps[2] = 2
        else:
            if n == 1 or n == 0:
                return 1
            else:
                return 2
        for i in xrange(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
            
        return steps[n]
        """
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        prev1, prev2 = 1, 2
        for i in xrange(3, n+1):
            cur = prev1 + prev2
            prev1, prev2 = prev2, cur
        return cur
