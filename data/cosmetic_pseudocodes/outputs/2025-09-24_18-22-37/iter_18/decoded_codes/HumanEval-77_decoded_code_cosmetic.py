from math import copysign

def iscube(integer_value: int) -> bool:
    # Work with the absolute value for cube root
    temp_var1: int = -integer_value if integer_value < 0 else integer_value

    # Compute the cube root with sign consideration
    cube_root: float = copysign(abs(temp_var1) ** (1/3), integer_value)
    temp_var3: int = round(cube_root)

    # Check if the cube of the rounded root matches the original integer value
    return temp_var3 ** 3 == integer_value