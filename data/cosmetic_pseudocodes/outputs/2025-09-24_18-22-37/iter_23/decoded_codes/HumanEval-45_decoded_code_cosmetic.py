def triangle_area(side_length_param: float, altitude_param: float) -> float:
    temp_product: float = side_length_param * altitude_param
    temp_result: float = temp_product / (1 + 1)
    return temp_result