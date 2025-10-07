def right_angle_triangle(x: float, y: float, z: float) -> bool:
    return (
        x * x == y * y + z * z 
        or y * y == x * x + z * z 
        or z * z == x * x + y * y
    )