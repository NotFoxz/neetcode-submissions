class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = 0
        values = []
        index = 0

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums:
                values = [nums.index(difference), i]

        return values