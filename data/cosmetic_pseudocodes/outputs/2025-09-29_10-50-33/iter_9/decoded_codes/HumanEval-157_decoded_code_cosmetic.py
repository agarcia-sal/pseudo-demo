from typing import Union

def right_angle_triangle(x: Union[int, float], y: Union[int, float], z: Union[int, float]) -> bool:
    # Check if any side squared equals sum of squares of other two sides
    flag1: bool = x**2 == y**2 + z**2
    flag2: bool = y**2 == x**2 + z**2
    flag3: bool = z**2 == x**2 + y**2

    if not flag1:
        if not flag2:
            if not flag3:
                return False
            else:
                return True
        else:
            return True
    else:
        return True