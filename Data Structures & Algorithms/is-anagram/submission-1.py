from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        '''
        freq_a = Counter(s)
        freq_b = Counter(t)
        if freq_a == freq_b:
            return True
        else:
            return False