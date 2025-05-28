class Solution:
    def search(self, nums, target):
        # IMPORTANT POINTS:
        # 1. Binary search only works on sorted arrays
        # 2. We use two pointers (l and r) to define our search space
        # 3. The middle point (m) helps us divide the search space in half
        
        l, r = 0, len(nums) - 1  # Initialize pointers at start and end of array

        while l <= r:  # Continue until pointers cross each other
            # IMPORTANT: Using this formula instead of (l + r) // 2 to prevent integer overflow
            # This is especially important in languages with fixed integer sizes
            m = l + ((r - l) // 2)  

            # Three possible cases:
            # 1. If middle number is greater than target, search in left half
            # 2. If middle number is less than target, search in right half
            # 3. If middle number equals target, we found our answer!
            if nums[m] > target:
                r = m - 1  # Move right pointer to left of middle
            elif nums[m] < target:
                l = m + 1  # Move left pointer to right of middle
            else:
                return m  # Found the target!
            
        return -1  # Target not found in array
    
# Test cases
sol = Solution()
nums = [-1,0,2,4,6,8,10]
target = 10

x = sol.search(nums, target)
print(x)

# IMPORTANT COMPLEXITY ANALYSIS:
# Time Complexity: O(log n) - we are halving the search space with each iteration
# Space Complexity: O(1) - we are not using any extra space

# KEY TAKEAWAYS:
# 1. Binary search is much faster than linear search for sorted arrays
# 2. The search space is reduced by half in each iteration
# 3. The loop condition (l <= r) ensures we check all possible positions
# 4. The middle point calculation is crucial for efficiency
# 5. This algorithm is used in many real-world applications like:
#    - Searching in databases
#    - Finding items in sorted lists
#    - Implementing autocomplete features
#    - Game development for collision detection