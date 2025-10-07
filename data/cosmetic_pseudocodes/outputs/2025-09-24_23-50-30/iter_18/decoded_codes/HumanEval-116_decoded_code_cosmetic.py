from typing import List, Dict

def sort_array(collection_of_numbers: List[int]) -> List[int]:
    helper_map: Dict[int, int] = {}
    index_counter: int = 0
    length: int = len(collection_of_numbers)

    while index_counter < length:
        current_val = collection_of_numbers[index_counter]
        binary_str = bin(current_val)
        # Count '1's from 3rd index onward (0-based), i.e., skipping '0b' prefix and next char
        helper_map[current_val] = binary_str[3:].count('1')
        index_counter += 1

    # Copy input list to avoid mutating original
    first_sorted_list: List[int] = collection_of_numbers[:]
    position: int = 1

    while position < length:
        key_cmp = first_sorted_list[position]
        move_pos = position - 1
        while move_pos >= 0 and helper_map[first_sorted_list[move_pos]] > helper_map[key_cmp]:
            first_sorted_list[move_pos + 1] = first_sorted_list[move_pos]
            move_pos -= 1
        first_sorted_list[move_pos + 1] = key_cmp
        position += 1

    return first_sorted_list