#https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        last = len(nums) - 1
        ans = nums[0]+nums[1]+nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = last
            while left < right:

                candidate = nums[left] + nums[right] + nums[i]

                if abs(target - candidate) < abs(target - ans):
                    ans = candidate

                if candidate == target:
                    return candidate
                
                if candidate > target:
                    right = right - 1
                else:
                    left = left + 1
        return ans


