def has_close_elements(nums, thr):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and abs(nums[i] - nums[j]) < thr:
                return True
    return False