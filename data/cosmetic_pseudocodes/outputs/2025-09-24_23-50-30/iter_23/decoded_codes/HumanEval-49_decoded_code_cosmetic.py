def modp(arg_x: int, arg_y: int) -> int:
    result_accumulator: int = 1
    integer_counter: int = 0
    while integer_counter < arg_x:
        doubled = result_accumulator * 2
        result_accumulator = doubled - (doubled // arg_y) * arg_y
        integer_counter += 1
    return result_accumulator