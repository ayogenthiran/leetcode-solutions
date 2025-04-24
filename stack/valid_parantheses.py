class Solution:
    def isValid(self,s):
        stack = []
        closeToopen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToopen:
                if stack and stack[-1] == closeToopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
# Test

sol = Solution()
s = "([{}])" 

x = sol.isValid(s)
print(x)

w = "[(])"
y = sol.isValid(w)
print(y)

