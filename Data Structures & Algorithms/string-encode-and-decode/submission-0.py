class Solution:

    def encode(self, strs: List[str]) -> str:
        stringTracker = ""
        for i in strs:
            stringTracker += str(len(i)) + "#" + i
        return stringTracker      


    def decode(self, s: str) -> List[str]:
        listTracker = []
        i = 0
        j = 0
        previousNumber = ""
        currentWord = ""
        while i < len(s):
            if s[i] == "#":
                if previousNumber.isdigit():
                    j = i
                    increment = j + int(previousNumber) + 1
                    while j < int(increment):
                        j += 1
                i += 1
                currentWord += s[i:j]
                listTracker.append(currentWord)
                previousNumber = ""
                currentWord = ""
                i = j
            else: 
                previousNumber += s[i]
                i += 1
        return listTracker           
