class Solution:
    def maxArea(self, heights):
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res
    
# Test
sol = Solution()
heights = [1,8,6,2,5,4,8,3,7]
x = sol.maxArea(heights)
print(x)




