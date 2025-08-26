class Solution:
    def maxArea(self, heights):
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(area, max_area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_area
    
# Test
sol = Solution()
heights = [1,8,6,2,5,4,8,3,7]
x = sol.maxArea(heights)
print(x)