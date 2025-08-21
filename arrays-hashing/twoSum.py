class Solution:
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
                
    
# Test
sol = Solution()
nums = [3,4,5,6]
target = 7
x = sol.twoSum(nums, target)
print(x)

# Time Complexity: O(n)
# Space Complexity: O(n)