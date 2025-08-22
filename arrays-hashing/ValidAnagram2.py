from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        countS = Counter(s) 
        countT = Counter(t)

        return countS == countT
    


#Testing the case
sol = Solution()

s = "racecar"
t = "carrace"
x = sol.isAnagram(s,t)
print(x)
