import math

def triangle_area(a, b, c):
    # Check if the given sides form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate semi-perimeter
    s = (a + b + c) / 2

    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Round the area to 2 decimal places
    return round(area, 2)