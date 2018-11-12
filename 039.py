"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = []
        
        def helper(number, candidates):
            if number == 0:
                return
            temp = []
            for i in candidates:
                if number-i >= 0:
                    if dp[number-i]:
                        for e in dp[number-i]:
                            temp.append([i]+e)
                    elif number == i:
                        temp.append([i])
            h = set()
            ans = []
            for e in temp:
                #print e
                d = tuple(sorted(e))
                if d not in h:
                    h.add(d)
                    ans.append(e)
            dp[number] = ans
        
        for _ in xrange(target+1):
            dp.append([])
            
        for i in xrange(target+1):
            helper(i, candidates)
            #print dp
        
        return dp[target]
