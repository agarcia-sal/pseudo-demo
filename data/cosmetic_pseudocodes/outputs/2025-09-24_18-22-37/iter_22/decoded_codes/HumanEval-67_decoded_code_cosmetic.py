from typing import List


def fruit_distribution(text_data: str, quantity_fruits: int) -> int:
    numeric_entries: List[int] = []
    pieces = text_data.split(" ")
    iterator_index = 0
    while iterator_index < len(pieces):
        current_piece = pieces[iterator_index]
        if not (current_piece < "0" or current_piece > "9"):  # current_piece is digit string
            temp_str = current_piece
            decimal_base = 10
            converted_number = 0
            char_index = 0
            while char_index < len(temp_str):
                char_val = ord(temp_str[char_index]) - ord("0")
                converted_number = converted_number * decimal_base + char_val
                char_index += 1
            numeric_entries.append(converted_number)
        iterator_index += 1
    total_sum = 0
    sum_index = 0
    while sum_index < len(numeric_entries):
        total_sum += numeric_entries[sum_index]
        sum_index += 1
    return quantity_fruits - total_sum