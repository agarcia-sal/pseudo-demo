def iscube(a: int) -> bool:
    """
    Check if the absolute value of 'a' is a perfect cube.

    Args:
        a (int): The input integer.

    Returns:
        bool: True if abs(a) is a perfect cube, False otherwise.
    """
    a = abs(a)
    # Calculate the integer nearest to the cube root of 'a'
    cube_root = round(a ** (1/3))
    # Check if cube_root ** 3 equals 'a'
    return cube_root ** 3 == a