"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        s1 = strs[0]
        s2 = strs[-1]
        end = 0
        for i in xrange(min(len(s1), len(s2))):
            if s1[i] == s2[i]: end += 1
            else: break
        return s1[:end] if end > 0 else ""
            
