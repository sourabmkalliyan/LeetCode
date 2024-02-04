class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] != 1:
                ans = max(count, ans)
                count = 0
        return max(count, ans)