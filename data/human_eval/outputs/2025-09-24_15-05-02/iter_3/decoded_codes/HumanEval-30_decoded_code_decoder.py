def get_positive(numbers):
    """
    Returns a list of positive numbers from the input list.

    Parameters:
    numbers (list): List of numerical values.

    Returns:
    list: A list containing only the positive numbers from the input list.
    """
    return [num for num in numbers if num > 0]