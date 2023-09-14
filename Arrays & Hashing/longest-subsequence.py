#https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}
        for i in nums:
            num_dict[i] = 1
            
        ans = 0
        for i in nums:
            x = i
            candidate = 0
            while num_dict.get(x,0):
                candidate = candidate + num_dict[x]
                num_dict[x] = 0
                x = x - 1
            num_dict[i] = candidate
            if ans < candidate:
                ans = candidate
        return ans