"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

"""



class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        lastItem = nums[0]
        res = []
        start = end = 0
        for i in xrange(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                end += 1
            else:
                if start == end:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + "->" +str(nums[end]))
                start = end = i
        if start == end:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start])+"->"+str(nums[end]))
            
        return res
        
