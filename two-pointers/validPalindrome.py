class Solution:
    def isPalindrome(self,s):

        left,right = 0, len(s) - 1  
        while left < right:

            while left < right and not self.isalnum(s[left]): # Skip non-alphanumeric from left
                left += 1
            while left > right and not self.isalnum(s[right]): # Skip non-alphanumeric from right
                right -= 1
            if s[left].lower() != s[right].lower():  # Compare characters (case-insensitive)
                return False
            
            # Move both pointers inward
            left += 1
            right -= 1
        return True  

    def isalnum(self,c):
        return ( ord('A') <= ord(c) <= ord('Z') or
                 ord('a') <= ord(c) <= ord('z') or
                 ord('0') <= ord(c) <= ord('9') )    
# Test
sol = Solution()
s = "tab a cat"
x = sol.isPalindrome(s)
print(x)

# Notes:
# - Two-pointer technique: O(n) time, O(1) space
# - Skip non-letters/numbers with isalnum()
# - Use .lower() for case-insensitive comparison


