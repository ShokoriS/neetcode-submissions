class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        frequency = {}

        i = 0 
        while i < len(s):
            frequency[s[i]] = frequency.get(s[i], 0) + 1
            frequency[t[i]] = frequency.get(t[i], 0) - 1
        
            i += 1
        print(frequency)
        for key, values in frequency.items():
            if values != 0:
                return False 

        return True 
            


