from math import sqrt
from typing import Union


def triangle_area(edge_x: float, edge_y: float, edge_z: float) -> Union[float, int]:
    if not (edge_x + edge_y > edge_z and edge_x + edge_z > edge_y and edge_y + edge_z > edge_x):
        return -1
    half_perimeter: float = (edge_x + edge_y + edge_z) / 2
    raw_area: float = sqrt(half_perimeter * (half_perimeter - edge_x) * (half_perimeter - edge_y) * (half_perimeter - edge_z))
    precise_area: float = round(raw_area, 2)
    return precise_area