class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        leftsum = 0
        for i, v in enumerate(nums):
            # leftsum == rightsum
            if leftsum == totalsum - leftsum - v:
                return i
            leftsum += v
        return -1
