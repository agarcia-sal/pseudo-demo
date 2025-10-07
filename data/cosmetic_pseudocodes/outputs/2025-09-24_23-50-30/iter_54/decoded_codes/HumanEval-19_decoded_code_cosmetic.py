from typing import List, Dict


def sort_numbers(str_input: str) -> str:
    digits_map: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    filtered_words: List[str] = [word for word in str_input.split(' ') if word != '']

    def merge_sort(arr: List[str]) -> List[str]:
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left_part = merge_sort(arr[:mid])
        right_part = merge_sort(arr[mid:])

        merged_result: List[str] = []
        i = j = 0
        while i < len(left_part) and j < len(right_part):
            if digits_map[left_part[i]] <= digits_map[right_part[j]]:
                merged_result.append(left_part[i])
                i += 1
            else:
                merged_result.append(right_part[j])
                j += 1

        merged_result.extend(left_part[i:])
        merged_result.extend(right_part[j:])
        return merged_result

    sorted_words = merge_sort(filtered_words)
    return ' '.join(sorted_words)