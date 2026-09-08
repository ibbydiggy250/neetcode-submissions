import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        s = [char for char in s if char not in string.punctuation]
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False