from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    auxiliary_collection: List[int] = []
    tokens: List[str] = string_description.split(" ")

    current_index: int = 0
    while current_index < len(tokens):
        current_token: str = tokens[current_index]
        is_digit_flag: bool = True

        for position in range(len(current_token)):
            if not ("0" <= current_token[position] <= "9"):
                is_digit_flag = False
                break

        if is_digit_flag:
            numeric_value: int = 0
            multiplier: int = 1
            digit_pos: int = len(current_token) - 1

            while digit_pos >= 0:
                char_code: int = ord(current_token[digit_pos]) - ord("0")
                numeric_value += char_code * multiplier
                multiplier *= 10
                digit_pos -= 1

            auxiliary_collection.append(numeric_value)

        current_index += 1

    sum_of_numbers: int = 0
    i: int = 0
    while i < len(auxiliary_collection):
        sum_of_numbers += auxiliary_collection[i]
        i += 1

    return total_number_of_fruits - sum_of_numbers