# Search in Rotated Sorted Array
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:  
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1       
    
# Test cases
sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0)) # Output: 4
print(sol.search([4,5,6,7,0,1,2], 3)) # Output: -1
print(sol.search([1], 0)) # Output: -1  

# Time Complexity: O(log n)
# Space Complexity: O(1)

