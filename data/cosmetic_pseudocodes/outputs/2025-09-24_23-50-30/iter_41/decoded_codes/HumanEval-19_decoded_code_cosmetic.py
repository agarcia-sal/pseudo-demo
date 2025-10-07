from typing import List, Dict

def sort_numbers(alpha_sequence: str) -> str:
    mapping_dictionary: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    processed_array: List[str] = [token for token in alpha_sequence.split(' ') if token]

    def merge_sort(arr: List[str]) -> List[str]:
        if len(arr) <= 1:
            return arr
        mid_index = len(arr) // 2
        left_part = merge_sort(arr[:mid_index])
        right_part = merge_sort(arr[mid_index:])
        merged_list: List[str] = []
        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left_part) or right_cursor < len(right_part):
            if right_cursor >= len(right_part) or (left_cursor < len(left_part) and mapping_dictionary[left_part[left_cursor]] <= mapping_dictionary[right_part[right_cursor]]):
                merged_list.append(left_part[left_cursor])
                left_cursor += 1
            else:
                merged_list.append(right_part[right_cursor])
                right_cursor += 1
        return merged_list

    ordered_list = merge_sort(processed_array)
    output_string = ' '.join(ordered_list)
    return output_string