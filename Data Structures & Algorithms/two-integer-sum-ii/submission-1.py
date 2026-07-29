class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            for l in range(len(numbers)):
                if numbers[l] == compliment:
                    return [i + 1, l + 1]
        
        