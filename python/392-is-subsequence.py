class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        end = len(s)
        if end == 0:
            return True

        for i in range(len(t)):
            if j >= end:
                break

            if t[i] == s[j]:
                j += 1
        
        return j == len(s)