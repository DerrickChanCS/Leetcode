"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        inp = str(num)
        from collections import defaultdict
        dict = defaultdict(lambda: -1)
        for i in xrange(len(inp)):
            dict[inp[i]] = max(dict[inp[i]], i)
        print dict
        for i in xrange(len(inp)):
            digit = inp[i]
            for j in xrange(9, int(digit), -1):
                k = str(j)
                #print dict[k]
                if dict[k] != -1 and dict[k] > i:
                    inp = list(inp)
                    inp[i], inp[dict[k]] = inp[dict[k]], inp[i]
                    #print inp
                    return int("".join(inp))
        return num
        """
        num = str(num)
        start = 0
        while num[start] == '9':
            start+=1
        least_sig = start
        least_digit = num[start]
        end = len(num) - 1
        from collections import defaultdict
        dict = defaultdict(lambda: -1)
        while end > start:
            if least_digit < num[end]:
                dict[num[end]] = max(dict[num[end]], end)
            end -= 1
        for i in xrange(int(least_digit)+1, 10):
            if dict[num[str(i)]] == -1:
                continue
            else:
                return int(nums[:start]+str(i))
        """    
            
