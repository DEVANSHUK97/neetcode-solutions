class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mn_speed = 1
        mx_speed = max(piles)

        while mn_speed <= mx_speed:
            speed = (mn_speed+mx_speed)//2
            time_taken = sum([math.ceil(pile/speed) for pile in piles])
            if time_taken <= h:
                mx_speed = speed - 1
            elif time_taken > h:
                mn_speed = speed + 1
        return mn_speed