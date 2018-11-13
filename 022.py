"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        dp = ["()"]
        
        for i in xrange(2, n+1):
            seen = set()
            res = []
            for p in dp:
                #print p
                prepend = "()"+p
                append = p+"()"
                if prepend not in seen:
                    seen.add(prepend)
                    res.append(prepend)
                if append not in seen:
                    seen.add(append)
                    res.append(append)
                #insert parens
                for j in xrange(len(p)):
                    #print "in loop", p
                    #print "p[j]", p[j]
                    if p[j] == "(":
                        #print "in if"
                        s = p[:j+1]+"()"+p[j+1:]
                        #print s
                        if s not in seen:
                            seen.add(s)
                            res.append(s)
            dp = res
        return dp
