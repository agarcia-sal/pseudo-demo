class Solution:
    def minOperations(self, nums: list[int]) -> int:
        totalLength = len(nums)
        counterOps = 0
        idx = 0

        def flipAt(arr: list[int], pos: int) -> None:
            arr[pos] = 1 - arr[pos]
            arr[pos + 1] = 1 - arr[pos + 1]
            arr[pos + 2] = 1 - arr[pos + 2]

        while idx < totalLength - 2:
            if nums[idx] == 0:
                flipAt(nums, idx)
                counterOps += 1
            idx += 1

        if nums[totalLength - 1] == 0 or nums[totalLength - 2] == 0:
            return -1

        return counterOps