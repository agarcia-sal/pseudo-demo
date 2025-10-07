from math import sqrt, floor
from typing import Union


def triangle_area(edge_one: float, edge_two: float, edge_three: float) -> Union[float, int]:
    if not (
        (edge_one + edge_two > edge_three)
        and (edge_one + edge_three > edge_two)
        and (edge_two + edge_three > edge_one)
    ):
        return -1

    half_perimeter: float = (edge_one + edge_two + edge_three) / 2
    root_expr: float = (
        half_perimeter
        * (half_perimeter - edge_one)
        * (half_perimeter - edge_two)
        * (half_perimeter - edge_three)
    )
    raw_area: float = sqrt(root_expr)

    final_result: float = floor(raw_area * 100 + 0.5) / 100

    return final_result