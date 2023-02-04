# Question

# 942. DI String Match
# Easy
# 2.1K
# 830
# Companies
# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

# Example 1:

# Input: s = "IDID"
# Output: [0,4,1,3,2]

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        numI = 0
        numD = len(s)
        ans = []
        for i in range(0,len(s)):
            if(s[i] == 'I'):
                ans.append(numI)
                numI=numI+1
            if(s[i] == 'D'):
                ans.append(numD)
                numD=numD-1
        if(s[len(s)-1] == 'I'):
            ans.append(numI)
        if(s[len(s)-1] == 'D'):
            ans.append(numD)

        return ans