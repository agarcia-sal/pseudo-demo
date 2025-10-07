def max_element(lst):
    """
    Returns the maximum element in the list.
    Assumes the list has at least one element.
    """
    max_value = lst[0]
    for element in lst:
        if element > max_value:
            max_value = element
    return max_value