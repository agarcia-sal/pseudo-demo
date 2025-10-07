def modp(integer_x: int, integer_y: int) -> int:
    final_result: int = 1
    iterator_counter: int = 0
    while iterator_counter < integer_x:
        intermediate_product: int = 2 * final_result
        final_result = intermediate_product % integer_y
        iterator_counter += 1
    return final_result