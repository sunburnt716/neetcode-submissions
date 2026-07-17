class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        frequent = [0]*k
        for i in nums:
            if i in tracker.keys():
                tracker[i] += 1
            else:
                tracker[i] = 1
        for c in range(k):
            key_to_pop = max(tracker, key=tracker.get)
            frequent[c] = key_to_pop
            tracker.pop(key_to_pop)
        return frequent
