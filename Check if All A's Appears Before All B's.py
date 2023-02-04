# Question
# 2124. Check if All A's Appears Before All B's
# Easy
# 544
# 13
# Companies
# Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

# Example 1:

# Input: s = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
# Hence, every 'a' appears before every 'b' and we return true.

class Solution:
    def checkString(self, s: str) -> bool:
        sortedString = sorted(s)
        sortedString = "".join(sortedString)
        print(sortedString)
        if(s == sortedString):
            return True
        else:
            return False