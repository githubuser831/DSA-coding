class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                checker = nums[i] + nums[j] 
                if checker == target:
                    solution.append(i)
                    solution.append(j)
                    return  solution
