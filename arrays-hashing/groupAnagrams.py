from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Create a special dictionary that automatically creates empty lists for new keys
        # This helps us group words without checking if the key exists first
        res = defaultdict(list)

        # Iterate through each word in the input list
        for s in strs:
            # Create a list of 26 zeros to count occurrences of each letter (a-z)
            # Each index represents a letter (0=a, 1=b, 2=c, etc.)
            count = [0] * 26

            # Count the frequency of each letter in the current word
            for c in s:
                # Convert letter to index (a=0, b=1, c=2, etc.)
                # Increment the count for that letter
                count[ord(c) - ord('a')] += 1

            # Convert count list to tuple (because lists can't be dictionary keys)
            # Add the current word to the list of words with the same letter counts
            res[tuple(count)].append(s)

        # Return all the groups of anagrams
        return res.values()


# Test the solution
sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
x = sol.groupAnagrams(strs)
print(x)

# Time Complexity: O(m*n) where:
# - m is the number of words in the input list
# - n is the length of the longest word
# Space Complexity: O(m) where:
# - m is the number of words we need to store in our result