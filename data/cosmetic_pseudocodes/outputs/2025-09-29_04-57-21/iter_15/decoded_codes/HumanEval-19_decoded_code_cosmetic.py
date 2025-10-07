from typing import List


def sort_numbers(string_of_number_words: str) -> str:
    numeral_values: dict[str, int] = {
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

    split_tokens: List[str] = string_of_number_words.split(' ')
    filtered_tokens: List[str] = [token for token in split_tokens if token != '']

    def compare_words(a: str, b: str) -> int:
        return numeral_values[a] - numeral_values[b]

    # Python's sorted doesn't use a comparator but a key function,
    # so we sort by numeral_values directly
    ordered_tokens: List[str] = sorted(filtered_tokens, key=lambda x: numeral_values[x])

    result_str: str = ' '.join(ordered_tokens)
    return result_str