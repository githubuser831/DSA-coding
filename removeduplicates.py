class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n - 1):

            j = i + 1

            if j == len(nums):
                return
            else:
                while nums[i] == nums[j]:
                    nums.pop(i)
                    if j == len(nums):
                        return
