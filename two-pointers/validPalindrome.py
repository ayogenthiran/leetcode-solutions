class Solution:
    def isPalindrome(self,s):

        left,right = 0, len(s) - 1  
        while left < right:

            while left < right and not self.isalnum(s[left]):
                left += 1
            while left > right and not self.isalnum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
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

# Time Complexity: O(n)
# Space Complexity: O(1)    

