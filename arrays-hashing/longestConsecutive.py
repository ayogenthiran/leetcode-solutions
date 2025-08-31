class Solution:
    def longestConsecutive(self, nums):
        numset = set(nums)
        longest = 0

        for n in numset:
            if (n-1) not in numset:
                length = 0
                while (length + n) in numset:
                    length += 1
                longest = max(length, longest)
        return longest
    

# Test
nums=[2,20,4,10,3,4,5]
sol = Solution()
x = sol.longestConsecutive(nums)
print(x)



            