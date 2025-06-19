class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
    
# Test
sol = Solution()
s = "tab a cat"
x = sol.isPalindrome(s)
print(x)