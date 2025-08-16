#  Two Sum II - Input Array Is Sorted   

class Solution:
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left < right:
            sum = nums[left] + nums[right]
            # If the sum is smaller, increment the left pointer, aiming to increase the sum toward the target value
            if sum < target:
                left += 1
            # If the sum is greater, decrement the right pointer, aiming to decrease the sum toward the target value
            elif sum > target:
                right -= 1 
            # If the taregt pair is found, retuen the indexes     
            else:
                return [left, right]
        return [] 

    
# Test
sol = Solution()
nums = [-5, -2, 3, 4, 6]
target = 7
x = sol.twoSum(nums, target)
print(x)

    # Time Complexity: O(n)
    # Space Complexity: O(1)