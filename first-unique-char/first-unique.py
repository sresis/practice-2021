class Solution:
    def firstUniqChar(self, s: str) -> int:
        # make a dict of each letter and indexes
        chars = {}
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]].append(i)
            else:
                chars[s[i]] = [i]
        for i in range(len(s)):
            if len(chars[s[i]]) == 1:
                return i
        return -1
