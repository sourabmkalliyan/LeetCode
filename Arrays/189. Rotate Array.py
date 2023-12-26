class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        self.reverse(n, nums, 0, n - 1)
        self.reverse(n, nums, 0, k-1)
        self.reverse(n, nums, k, n-1)
    def reverse(self, n:int, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1