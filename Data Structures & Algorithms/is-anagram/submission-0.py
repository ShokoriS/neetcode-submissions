class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        seen =  {}

        for letter in s1:
            seen[letter] = seen.get(letter, 0) + 1


        for letter in s2:
            if seen.get(letter, 0) == 0:
                return False

            seen[letter]-=1
        return True
        