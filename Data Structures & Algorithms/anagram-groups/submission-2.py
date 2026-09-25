class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for i in strs:
            normalizer = "".join(sorted(i))
            if normalizer in tracker:
                tracker[normalizer].append(i)
            else:
                newList: List[str] = []
                newList.append(i)
                tracker[normalizer] = newList
        return list(tracker.values())
