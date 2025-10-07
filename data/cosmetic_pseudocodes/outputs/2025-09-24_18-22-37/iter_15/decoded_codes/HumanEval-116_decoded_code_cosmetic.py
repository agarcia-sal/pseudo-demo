from typing import List, Tuple


def sort_array(array_of_integers: List[int]) -> List[int]:
    temp_result: List[Tuple[int, int]] = []
    temp_numbers: List[int] = []

    index_i: int = 0
    while index_i < len(array_of_integers):
        temp_numbers.append(array_of_integers[index_i])
        index_i += 1

    bubble_sort_ascending(temp_numbers)

    index_j: int = 0
    while index_j < len(temp_numbers):
        current_element: int = temp_numbers[index_j]
        binary_string_representation: str = CONVERT_TO_BINARY(current_element)
        trimmed_binary_string: str = binary_string_representation[2:-2] if len(binary_string_representation) > 4 else ""

        count_of_ones: int = 0
        k: int = 0
        while k < len(trimmed_binary_string):
            if trimmed_binary_string[k] == '1':
                count_of_ones += 1
            k += 1

        temp_result.append((current_element, count_of_ones))
        index_j += 1

    sort_by_secondary_key(temp_result)

    final_array: List[int] = []
    m: int = 0
    while m < len(temp_result):
        final_array.append(temp_result[m][0])
        m += 1

    return final_array


def bubble_sort_ascending(numbers: List[int]) -> None:
    n: int = len(numbers)
    x: int = n - 1

    while x > 0:
        y: int = 0
        while y < x:
            if numbers[y] > numbers[y + 1]:
                temp_val: int = numbers[y]
                numbers[y] = numbers[y + 1]
                numbers[y + 1] = temp_val
            y += 1
        x -= 1


def sort_by_secondary_key(pairs: List[Tuple[int, int]]) -> None:
    length_pairs: int = len(pairs)
    outer_index: int = 0
    while outer_index < length_pairs - 1:
        inner_index: int = 0
        while inner_index < length_pairs - outer_index - 1:
            current_count: int = pairs[inner_index][1]
            next_count: int = pairs[inner_index + 1][1]

            if current_count > next_count:
                temp_pair: Tuple[int, int] = pairs[inner_index]
                pairs[inner_index] = pairs[inner_index + 1]
                pairs[inner_index + 1] = temp_pair
            inner_index += 1
        outer_index += 1


def CONVERT_TO_BINARY(number: int) -> str:
    result_string: str = ""
    quotient: int = number

    if quotient == 0:
        return "0b0"

    while quotient > 0:
        remainder: int = quotient % 2
        remainder_char: str = "0" if remainder == 0 else "1"
        result_string = remainder_char + result_string
        quotient = quotient // 2

    return "0b" + result_string