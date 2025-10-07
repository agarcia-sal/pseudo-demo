def triples_sum_to_zero(nums):
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1
    return False