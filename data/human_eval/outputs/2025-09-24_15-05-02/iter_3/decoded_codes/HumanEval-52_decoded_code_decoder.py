def below_threshold(values: list[int], threshold: int) -> bool:
    """
    Returns True if all elements in the list are less than the threshold,
    otherwise returns False.
    """
    for value in values:
        if value >= threshold:
            return False
    return True