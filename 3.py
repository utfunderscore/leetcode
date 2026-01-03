class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenBefore = set([])
        left = 0
        best = 0
        for i, c in enumerate(s):
            if c in seenBefore:
                while c in seenBefore:
                    seenBefore.remove(s[left])
                    left+=1
            seenBefore.add(c)
            best = max(best, i-left+1)

        return best
