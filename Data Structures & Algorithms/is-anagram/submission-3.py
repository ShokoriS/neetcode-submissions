class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
        
        frequency_s = {}
        frequency_t = {}
        s = s.lower()
        t = t.lower()
        i = 0 
        while i < len(s):
            frequency_s[s[i]] = frequency_s.get(s[i], 0) + 1
            frequency_t[t[i]] = frequency_t.get(t[i], 0) + 1
            
            i += 1 

        i = 0 
        while i < len(frequency_s):

            if frequency_s.get(s[i]) != frequency_t.get(s[i]):
                return False 
            i += 1
        return True 


         


