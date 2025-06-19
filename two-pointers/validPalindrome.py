class Solution:
    def is_palindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.is_alpha_num(s[l]):
                l += 1
            while r > l and not self.is_alpha_num(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1 
        return True
        
    def is_alpha_num(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        
# Test
sol = Solution()
s = "tab a cat"
x = sol.is_palindrome(s)
print(x)

# Time Complexity: O(n)
# Space Complexity: O(1)    

