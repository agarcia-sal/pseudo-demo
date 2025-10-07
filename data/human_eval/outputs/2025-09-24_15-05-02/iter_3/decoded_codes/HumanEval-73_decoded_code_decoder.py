def smallest_change(arr):
    """
    Counts the number of positions in the first half of the list where the element
    does not match the corresponding element from the end.

    Args:
        arr (list): The input list to check.

    Returns:
        int: The count of mismatched pairs.
    """
    ans = 0
    length = len(arr)
    # Iterate over the first half of the list
    for i in range(length // 2):
        if arr[i] != arr[length - i - 1]:
            ans += 1
    return ans