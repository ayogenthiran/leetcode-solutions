class Solution:
    def maxArea(self, heights):
        res = 0
        l, r = 0, len(heights)-1

        while l<r:
            area = min(heights[l], heights[r]) * (r-l) # Finding the area using minimum height
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
    

# Test
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
x = sol.maxArea(height)
print(x)