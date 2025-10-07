def triangle_area(side_len: float, h_t: float) -> float:
    temp_product: float = h_t * side_len
    result_accumulator: float = temp_product * 0.5
    return result_accumulator