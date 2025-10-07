from typing import List, Dict

def sort_numbers(p_input: str) -> str:
    value_map: Dict[str, int] = {
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

    def quicksort(arr: List[str]) -> List[str]:
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = quicksort([x for x in arr[1:] if value_map[x] < value_map[pivot]])
        right = quicksort([x for x in arr[1:] if value_map[x] >= value_map[pivot]])
        return left + [pivot] + right

    temp_list: List[str] = []
    word = ''
    for ch in p_input + ' ':
        if ch != ' ':
            word += ch
        elif word != '':
            temp_list.append(word)
            word = ''
    filtered_tokens = [x for x in temp_list if x != '']
    ordered_list = quicksort(filtered_tokens)
    return ' '.join(ordered_list)