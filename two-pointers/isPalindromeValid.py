class Solution:
    def is_Palindrome(self, s):
        left, right = 0, len(s) - 1
        # Two-pointer technique to check for palindrome
        # Skip non-alphanumeric characters and compare characters
        # in a case-insensitive manner  
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
        
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    
        return True
    

# Test
sol = Solution()
s = "A man, a plan, a canal: Panama" 
x = sol.is_Palindrome(s)
print(x)  # Output: True