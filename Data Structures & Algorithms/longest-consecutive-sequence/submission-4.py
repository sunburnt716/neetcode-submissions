class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        previous = nums[0]
        counter = 1
        largestConsecutive = 0
        tracker = []
        for i in nums:
            if i == previous + 1:
                counter += 1
            elif i == previous:
                counter = counter
            else:
                counter = 1
            previous = i
            if counter > largestConsecutive:
                largestConsecutive = counter
        return largestConsecutive 

            
        