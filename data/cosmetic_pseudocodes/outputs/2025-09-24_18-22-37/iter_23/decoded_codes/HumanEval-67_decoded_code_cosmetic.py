from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    temporary_results: List[int] = []
    tokens_list: List[str] = string_description.split(" ")
    index_position: int = 0

    while index_position < len(tokens_list):
        current_token = tokens_list[index_position]
        if not current_token.isdigit():
            numeric_value = 0
            char_position = 0
            numeric_string = current_token
            while char_position < len(numeric_string):
                current_char = numeric_string[char_position]
                digit_value = 0
                if '0' <= current_char <= '9':
                    digit_value = ord(current_char) - ord('0')
                numeric_value = numeric_value * 2 + digit_value
                char_position += 1
            temporary_results.append(numeric_value)
        index_position += 1

    sum_of_numbers = 0
    position_counter = 0
    while position_counter < len(temporary_results):
        sum_of_numbers += temporary_results[position_counter]
        position_counter += 1

    result_value = total_number_of_fruits - sum_of_numbers
    return result_value