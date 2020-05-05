class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        look = defaultdict(int)
        char = set()
        for i, c in enumerate(s):
            if look[c]:
                char.discard(look[c])
            else:
                look[c] = i+1
                char.add(i+1)

        return min(char)-1 if char else -1
