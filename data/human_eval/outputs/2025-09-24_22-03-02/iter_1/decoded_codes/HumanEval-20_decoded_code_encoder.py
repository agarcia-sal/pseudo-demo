def find_min_diff_pair(numbers):
    sorted_nums = sorted(numbers)
    min_diff = abs(sorted_nums[1] - sorted_nums[0])
    pair = (sorted_nums[0], sorted_nums[1])
    for i in range(1, len(sorted_nums)):
        diff = abs(sorted_nums[i] - sorted_nums[i-1])
        if diff < min_diff:
            min_diff = diff
            pair = (sorted_nums[i-1], sorted_nums[i])
    return pair