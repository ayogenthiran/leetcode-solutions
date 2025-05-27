class Solution:
    def isValid(self, s):
        # Initialize an empty stack to keep track of opening brackets
        stack = []
        
        # Dictionary mapping closing brackets to their corresponding opening brackets
        # This helps us quickly check if a closing bracket matches the last opening bracket
        closeToopen = {")":"(", "]":"[", "}":"{"}

        # Iterate through each character in the input string
        for c in s:
            # Check if the current character is a closing bracket
            if c in closeToopen:
                # If we find a closing bracket, we need to check two things:
                # 1. Is there anything in our stack? (stack)
                # 2. Does the last opening bracket in our stack match this closing bracket?
                if stack and stack[-1] == closeToopen[c]:
                    # If both conditions are true, remove the matching opening bracket
                    stack.pop()
                else:
                    # If either condition is false, the string is invalid
                    return False
            else:
                # If the character is an opening bracket, add it to our stack
                stack.append(c)
        
        # After processing all characters, check if our stack is empty
        # If the stack is empty, all brackets were properly matched
        # If the stack is not empty, we have unmatched opening brackets
        return True if not stack else False
    

# Test
sol = Solution()
s = "([{}])"
x = sol.isValid(s)
print(x)

# Time Complexity: O(n) - we only iterate through the string once
# Space Complexity: O(n) - we use a stack to store the characters

# Example Walkthrough:
# Input: "([{}])"
# 1. "(" - Add to stack: stack = ["("]
# 2. "[" - Add to stack: stack = ["(", "["]
# 3. "{" - Add to stack: stack = ["(", "[", "{"]
# 4. "}" - Matches with "{", remove "{": stack = ["(", "["]
# 5. "]" - Matches with "[", remove "[": stack = ["("]
# 6. ")" - Matches with "(", remove "(": stack = []
# 7. Stack is empty, return True
