class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for i in strs:
            counter = [0] * 26
            for c in i:
                index = ord(c) - ord("a")
                counter[index] += 1
            key = tuple(counter)
            if key not in tracker:
                tracker[key] = []
            tracker[key].append(i)
        return list(tracker.values())