class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        charSet = set()
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

# Test cases
# "abcabcbb" -> 3
# "bbbbb" -> 1
# "pwwkew" -> 3    

if __name__ == "__main__":
    sol =  Solution()
    x = sol.lengthOfLongestSubstring("abcabcbb")
    print(x)

# Time complexity: O(n)
# Space complexity: O(m)
