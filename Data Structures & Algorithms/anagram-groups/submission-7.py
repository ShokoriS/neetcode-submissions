class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

# we will count the frequency of the char and return it as a tuple 
# if we have the same frequency tuple inside our dict which means it will have a list and we will just append the value to the end
# if not we will just create one with that tuple from frequency_counter and add the word into the list of value 

        def frequency_counter(s):
    
            char_frequency = [0] * 26
            

            i = 0 
            
            while i < len(s):
                if s[i].isalpha():
                    code = ord(s[i].lower()) - ord('a') 
                    char_frequency[code] += 1  
                i += 1

            return tuple(char_frequency) 

       
        anagrams = {}
        for word in strs:
           
            info = frequency_counter(word)
            if info in anagrams:
                anagrams[info].append(word)
            else:
                anagrams[info] = [word]
        gatherd_anagrams = []
        for value in anagrams.values():
            gatherd_anagrams.append(value)
        return gatherd_anagrams


   
    




