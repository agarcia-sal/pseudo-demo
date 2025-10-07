from typing import Dict

def sort_numbers(alphanumeric_blob: str) -> str:
    numeric_lookup: Dict[str, int] = {
        'one': 1,
        'seven': 7,
        'two': 2,
        'zero': 0,
        'five': 5,
        'six': 6,
        'three': 3,
        'eight': 8,
        'four': 4,
        'nine': 9,
    }
    fragment_collection = [token for token in alphanumeric_blob.split(' ') if token]
    ordered_fragments = sorted(fragment_collection, key=lambda x: numeric_lookup[x])
    result_string = ''
    index_variable = 0
    while index_variable < len(ordered_fragments):
        if index_variable != 0:
            result_string += ' '
        result_string += ordered_fragments[index_variable]
        index_variable += 1
    return result_string