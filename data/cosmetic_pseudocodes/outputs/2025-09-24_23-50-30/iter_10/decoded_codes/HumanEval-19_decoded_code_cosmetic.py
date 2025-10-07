from typing import List

def sort_numbers(input_string: str) -> str:
    mapping_dictionary: dict[str, int] = {
        'nine': 9,
        'eight': 8,
        'seven': 7,
        'six': 6,
        'five': 5,
        'four': 4,
        'three': 3,
        'two': 2,
        'one': 1,
        'zero': 0
    }

    def obtain_valid_tokens(phrase: List[str], index: int, acc: List[str]) -> List[str]:
        if index == len(phrase):
            return acc
        segment = phrase[index]
        if segment in mapping_dictionary and segment != '':
            return obtain_valid_tokens(phrase, index + 1, acc + [segment])
        else:
            return obtain_valid_tokens(phrase, index + 1, acc)

    tokens_filtered: List[str] = obtain_valid_tokens(input_string.split(' '), 0, [])

    def merge_sort(array: List[str]) -> List[str]:
        if len(array) < 2:
            return array
        mid_point = len(array) // 2
        left_part = merge_sort(array[:mid_point])
        right_part = merge_sort(array[mid_point:])

        def merge_arrays(left_array: List[str], right_array: List[str], merged_acc: List[str]) -> List[str]:
            if not left_array:
                return merged_acc + right_array
            if not right_array:
                return merged_acc + left_array
            first_left = mapping_dictionary[left_array[0]]
            first_right = mapping_dictionary[right_array[0]]
            if first_left <= first_right:
                return merge_arrays(left_array[1:], right_array, merged_acc + [left_array[0]])
            else:
                return merge_arrays(left_array, right_array[1:], merged_acc + [right_array[0]])

        return merge_arrays(left_part, right_part, [])

    final_sorted_tokens = merge_sort(tokens_filtered)

    return ' '.join(final_sorted_tokens)