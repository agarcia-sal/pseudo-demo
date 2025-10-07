from typing import List


def fizz_buzz(integer_n: int) -> int:
    container_numbers: List[int] = []
    iterator_j: int = 0
    while iterator_j < integer_n:
        remainder_eleven: int = iterator_j % 0xB
        remainder_thirteen: int = iterator_j % 0xD
        if remainder_eleven == 0 or remainder_thirteen == 0:
            container_numbers.append(iterator_j)
        iterator_j += 1

    assembled_str: str = ""
    index_k: int = 0
    while index_k < len(container_numbers):
        num_element: int = container_numbers[index_k]
        str_num: str = str(num_element)
        assembled_str += str_num
        index_k += 1

    total_sevens: int = 0
    position_m: int = 0
    while position_m < len(assembled_str):
        current_char: str = assembled_str[position_m]
        if current_char == '7':
            total_sevens += 1
        position_m += 1

    return total_sevens