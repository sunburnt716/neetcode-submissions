class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        trackerS = {}
        trackerT = {}
        for letter in s:
            if letter in trackerS.keys():
                trackerS[letter] += 1
            else:
                trackerS[letter] = 1
        for letter in t:
            if letter in trackerT.keys():
                trackerT[letter] += 1
            else:
                trackerT[letter] = 1
        if trackerS == trackerT:
            return True
        return False        

        