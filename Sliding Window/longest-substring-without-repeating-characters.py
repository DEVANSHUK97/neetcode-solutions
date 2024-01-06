class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        l = len(s)
        ans = 0
        counts = {}
        while right < l:
            if counts.get(s[right], -1) == -1:
                counts[s[right]] = 1
                right = right + 1
            else:
                ans = max(ans, right - left)
                left = left + 1
                right = left
                counts = {}
        ans = max(ans, right - left)

        return ans
