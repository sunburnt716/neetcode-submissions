class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for i in nums:
            if i in tracker.keys():
                return True
            tracker[i] = 1 
        return False
            