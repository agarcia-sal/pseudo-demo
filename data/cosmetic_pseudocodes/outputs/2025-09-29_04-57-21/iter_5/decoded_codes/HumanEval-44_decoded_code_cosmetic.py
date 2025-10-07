from typing import List


def change_base(integer_x: int, integer_base: int) -> str:
    string_accumulator: List[str] = []

    def convert_number(number: int) -> None:
        if number <= 0:
            return
        remainder = number % integer_base
        quotient = number // integer_base
        convert_number(quotient)
        string_accumulator.append(str(remainder))

    convert_number(integer_x)
    return "".join(string_accumulator)