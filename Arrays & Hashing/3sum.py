#https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        last = len(nums)-1
        nums = sorted(nums)
        ans = []
        prev = None
        for i in range(len(nums)-2):
            if prev == nums[i]:
                continue
            left = i + 1
            right = last
            while left < right:
                print(i, left, right)
                if nums[i]+nums[left]+nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]]) 
                    nextleft = min(left+1, last)
                    while nums[left] == nums[nextleft]:
                        nextleft = nextleft + 1
                        if nextleft >= last:
                            nextleft = last
                            break
                    left = nextleft

                    nextright = max(i+1,right - 1)
                    while nums[right] == nums[nextright]:
                        nextright = nextright - 1
                        if nextright <= i+1:
                            nextright = i + 1
                            break
                    right = nextright

                elif nums[i]+nums[left]+nums[right] > 0:
                    right = right - 1

                else:
                    left = left + 1
                prev = nums[i]
        return ans
    
