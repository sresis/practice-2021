class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        end = len(haystack) - length + 1
        i = 0
        while i < end:
            curr = haystack[i:i+length]
            if curr == needle:
                return i
            i += 1
        if needle == "":
            return 0
        else:
            return -1

