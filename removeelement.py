class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums.pop(i)
            else:
                i+= 1
            n = len(nums)

        return n
