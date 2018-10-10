"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #utilizing gauss' method
        # calculate the expected total of 0..n numbers
        # subtract the array and the leftover result will be missing number
        total = (len(nums))*(len(nums)+1)
        total = total / 2
        for i in nums:
            total = total - i
        return total
