"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        from collections import Counter
        dict = Counter(S)
        heap = []
        for key in dict:
            heapq.heappush(heap, (-dict[key], key))
        #print heap
        answer = ""
        count, lastLetter = heapq.heappop(heap)
        answer += lastLetter
        if count+1 != 0:
            heapq.heappush(heap, (count+1, lastLetter))
        #print heap
        while heap:
            #print heap[0][0]
            c, l = heapq.heappop(heap)
            #print l, c
            if l == lastLetter:
                #l, c = heapq.heappop(heap)
                #print "in loop ", heap[0][0]
                if not heap: 
                    print "can't do it boss ", answer
                    return ""
                c1, l1 = heapq.heappop(heap)
                answer += l1
                #print "answer in loop ", answer
                lastLetter = l1
                heapq.heappush(heap, (c, l))
                if c1+1 != 0:
                    heapq.heappush(heap, (c1+1, l1))
            else:
                #l,c = heapq.heappop(heap)
                answer += l
                lastLetter  = l
                if c+1 != 0:
                    heapq.heappush(heap, (c+1, l))
        return answer
