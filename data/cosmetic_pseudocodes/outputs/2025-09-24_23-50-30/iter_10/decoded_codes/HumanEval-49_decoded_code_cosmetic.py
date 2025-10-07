from typing import Union

def modp(integer_n: int, integer_p: int) -> int:
    result_accumulator: int = 1
    integer_counter: int = 0
    while integer_counter < integer_n:
        doubled = result_accumulator + result_accumulator
        quotient = doubled // integer_p  # Integer division for quotient
        # Expression reduces to doubled % integer_p but written as per pseudocode
        result_accumulator = doubled - quotient * integer_p + quotient * integer_p - quotient * integer_p
        integer_counter += 1
    return result_accumulator