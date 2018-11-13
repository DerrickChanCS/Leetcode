"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        
        #for _ in xrange(target+1):
        #    dp.append([])
        nums.sort()
        for i in xrange(target+1):
            #ans = []
            count = 0
            for e in nums:
                sumArray = i - e
                if sumArray < 0: continue
                if sumArray == 0:
                    #ans.append([e])
                    count += 1
                count += dp[sumArray]
                #for candidate in dp[sumArray]:
                    #ans.append(candidate+[e])
            dp[i] = count
        #print dp
        return dp[target]
