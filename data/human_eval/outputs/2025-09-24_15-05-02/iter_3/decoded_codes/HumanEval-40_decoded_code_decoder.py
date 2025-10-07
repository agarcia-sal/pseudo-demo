def triples_sum_to_zero(nums):
    """
    Checks if there exist three elements in the list that sum to zero.

    Args:
        nums (list of int): The list of integers to check.

    Returns:
        bool: True if such a triplet exists, False otherwise.
    """
    n = len(nums)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    return True
    return False