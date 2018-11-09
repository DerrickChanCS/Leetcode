"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
"""


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        i = 0
        ans = []
        if len(s) <= 1:
            return []
        while i < len(s) - 1:
            #print s[i:i+2]
            if s[i:i+2] == "++":
                #print s[:i]
                ans.append(s[:i]+"--"+s[i+2:])
            i+=1
        return ans
