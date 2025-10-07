from typing import List

def int_to_mini_roman(number: int) -> str:
    num: List[int] = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym: List[str] = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i: int = 12
    result_string: str = ""
    while number != 0:
        division_result: int = number // num[i]
        number %= num[i]
        while division_result != 0:
            result_string += sym[i]
            division_result -= 1
        i -= 1
    return result_string.lower()