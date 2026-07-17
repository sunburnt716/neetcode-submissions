class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        answer = []
        first = 0
        second = 0
        for counter, i in enumerate(nums):
            compliment = target - i
            if compliment in tracker.keys():
                first = tracker[compliment]
                second = counter
                return [first, second]
            else:
                tracker[i] = counter
        return None