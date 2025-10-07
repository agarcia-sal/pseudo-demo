def find_closest_elements(nums):
    dist, pair = float('inf'), ()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                d = abs(nums[i] - nums[j])
                if d < dist:
                    dist, pair = d, (min(nums[i], nums[j]), max(nums[i], nums[j]))
    return pair