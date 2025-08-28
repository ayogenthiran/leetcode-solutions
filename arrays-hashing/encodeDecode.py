class Solution:
    def encode(self,strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self,s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j 
        return res


# Test
x = ["neet", "code", "love", "you"]
s = Solution() 

encoded = s.encode(x)
print("Encoded:", encoded)

decoded = s.decode(encoded)
print("Decoded:", decoded)

print("Test Passed:", decoded == x)




# Time Complexity: O(N)  
#Space Complexity: O(N)  
   