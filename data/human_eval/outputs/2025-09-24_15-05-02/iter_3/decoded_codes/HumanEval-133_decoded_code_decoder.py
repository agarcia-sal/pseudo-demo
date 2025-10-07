import math

def sum_squares(lst):
    """
    Calculates the sum of the squares of the ceiling values of each element in the list.

    Parameters:
    lst (list of float): List of numerical values.

    Returns:
    int: Sum of squares of ceiling of each element.
    """
    total = 0
    for element in lst:
        rounded_element = math.ceil(element)
        total += rounded_element ** 2
    return total