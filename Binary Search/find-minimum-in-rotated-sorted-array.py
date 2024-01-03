class Solution:
    def findMin(self, nums: List[int]) -> int:
        mn = 0
        mx = len(nums) - 1
        while mn < mx:
            if nums[mn] < nums[mx]:
                return nums[mn]

            mid = (mn+mx)//2
            if nums[mid] > nums[mx]:
                mn = mid + 1
            else:
                mx = mid
        return nums[mn]
