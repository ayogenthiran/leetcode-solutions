class Solution:
    def threeSum(self, nums):
        # Initialize an empty list to store our results
        res = []
        # Sort the array first - this is crucial for our two-pointer approach
        nums.sort()

        # Iterate through each number in the array
        for i, a in enumerate(nums):
            # Skip if we've already processed this number before
            # This prevents duplicate triplets
            if i > 0 and a == nums[i-1]:
                continue

            # Set up two pointers:
            # l: starts from the next number after current number
            # r: starts from the end of the array
            l, r = i+1, len(nums)-1

            # While our pointers haven't crossed each other
            while l < r:
                # Calculate the sum of three numbers
                threeSum = a + nums[l] + nums[r]

                # If sum is too big, move right pointer left to get a smaller number
                if threeSum > 0:
                    r -= 1
                # If sum is too small, move left pointer right to get a bigger number
                elif threeSum < 0:
                    l += 1
                # If we found a valid triplet (sum = 0)
                else:
                    # Add the triplet to our results
                    res.append([a, nums[l], nums[r]])
                    # Move both pointers to find more combinations
                    l += 1
                    r -= 1

                    # Skip any duplicate numbers to avoid duplicate triplets
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res
    

# Test the solution
sol = Solution()
nums = [-1,0,1,2,-1,-4]
x = sol.threeSum(nums)
print(x)

# Time Complexity: O(n^2) - we have a nested loop structure
# Space Complexity: O(1) - we only use a constant amount of extra space





