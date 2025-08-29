class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# Test
x = [1,2,3,4]
sol = Solution()
output = sol.productExceptSelf(x)
print("output:", output)

# Time Complexity: O(n)
# Space Complexity: O(1) (excluding the output array)   