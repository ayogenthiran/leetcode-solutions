# Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + ((r-l)//2)
            if nums[m] < nums[r]:
                r = m
            else :
                l =m + 1
        return nums[l]
                    
# Tes
sol = Solution()
nums = [3,4,5,6,1,2]
nums_1 = [4,5,0,1,2,3]
nums_2 = [11,13,15,17]

x = sol.findMin(nums)
x_1 = sol.findMin(nums_1)
x_2 = sol.findMin(nums_2)

print(x)
print(x_1)
print(x_2)

# Time Complexity: O(log n)
# Space Complexity: O(1)