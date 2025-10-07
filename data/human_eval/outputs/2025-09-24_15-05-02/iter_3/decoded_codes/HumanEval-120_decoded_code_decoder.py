def maximum(arr, k):
    """
    Returns the k largest elements from the list arr in ascending order.
    If k is 0, returns an empty list.
    """
    if k == 0:
        return []
    # Sort the array in ascending order
    arr.sort()
    # Return the last k elements
    return arr[-k:]