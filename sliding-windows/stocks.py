class Solution:
    def maxProfit(self,prices):
        l,r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

# Tes
sol = Solution()
Prices = [10,1,5,6,7,1]
x = sol.maxProfit(Prices)
print(x)

# Time Complexity: O(n)
# Space Complexity: O(1)