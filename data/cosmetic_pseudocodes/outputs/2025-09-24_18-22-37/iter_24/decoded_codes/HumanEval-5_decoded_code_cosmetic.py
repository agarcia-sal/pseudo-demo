from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    output_container: List[int] = []
    flag_empty: bool = not list_of_numbers

    if flag_empty:
        return []

    index_counter: int = 1
    limit_index: int = len(list_of_numbers) - 1

    while index_counter <= limit_index:
        current_item: int = list_of_numbers[index_counter]
        temp_value: int = current_item
        output_container.append(temp_value)
        temp_delimiter: int = delimiter
        output_container.append(temp_delimiter)
        index_counter += 1

    temp_value = list_of_numbers[len(list_of_numbers) - 1]
    output_container.append(temp_value)

    return output_container