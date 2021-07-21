class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = ''
        for char in s:
            if char.isalnum():
                if char.isupper():
                    final += char.lower()
                else:
                    final += char
        return final == final[::-1]