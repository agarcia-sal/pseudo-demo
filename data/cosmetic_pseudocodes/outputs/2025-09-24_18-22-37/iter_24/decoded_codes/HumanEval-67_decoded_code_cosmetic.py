from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    collection_of_values: List[int] = []
    list_elements: List[str] = string_description.split(" ")
    index_counter: int = 0

    while index_counter < len(list_elements):
        current_entry: str = list_elements[index_counter]
        check_digit_flag: bool = False
        # Check if current_entry is a single character digit '0' through '9'
        if len(current_entry) == 1 and '0' <= current_entry <= '9':
            check_digit_flag = True
        else:
            check_digit_flag = False
        if check_digit_flag:
            temp_number: int = int(current_entry)
            collection_of_values.append(temp_number)
        index_counter += 1

    summation: int = 0
    iter_counter: int = 0
    while iter_counter < len(collection_of_values):
        current_value: int = collection_of_values[iter_counter]
        summation += current_value
        iter_counter += 1

    difference: int = total_number_of_fruits - summation
    return difference