"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numberMap = dict()
        for index, num in enumerate(nums):
            complement = target - num
            if complement in numberMap:
                return [numberMap[complement], index]
            else:
                numberMap[num] = index
        
