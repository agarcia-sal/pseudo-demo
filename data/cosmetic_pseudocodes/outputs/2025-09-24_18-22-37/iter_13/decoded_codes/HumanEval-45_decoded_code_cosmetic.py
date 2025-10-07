def triangle_area(side_length_param: float, altitude_param: float) -> float:
    intermediate_product: float = side_length_param * altitude_param
    divisor: int = 0x2
    computed_area: float = intermediate_product / divisor
    return computed_area