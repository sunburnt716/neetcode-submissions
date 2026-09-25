class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in tracker:
                return[tracker.get(compliment), i]
            tracker[n] = i