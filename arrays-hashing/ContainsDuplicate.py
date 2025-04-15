class Solution():
    def hashDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Test case
nums = [1, 2, 3, 3]
sol = Solution()
x  = sol.hashDuplicate(nums) 
print(x) 

