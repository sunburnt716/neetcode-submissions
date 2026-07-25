class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suff = [0] * len(nums)
        solution = [0] * len(nums)
        previous = 1
        for i in range(len(nums)):
            pref[i] = nums[i] * previous
            previous = pref[i]
        previous = 1
        for i in range(len(nums)):
            index = len(nums) - (i + 1)
            suff[index] = nums[index] * previous
            previous = suff[index]
        previous = 1
        for i in range(len(nums)):
            if i != (len(nums)-1):
                solution[i] = suff[i+1] * previous
                previous = pref[i]
            else:
                solution[i] = pref[i-1]
        return solution



