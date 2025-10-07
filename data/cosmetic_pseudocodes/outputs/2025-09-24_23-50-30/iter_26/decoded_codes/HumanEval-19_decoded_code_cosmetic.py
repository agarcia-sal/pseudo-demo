from typing import List, Dict

def sort_numbers(alphanumeric_sequence: str) -> str:
    digit_values: Dict[str, int] = {
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

    def extract_valid_terms(source_text: str, index: int, acc: List[str]) -> List[str]:
        if index >= len(source_text):
            return acc
        next_space = source_text.find(' ', index)
        if next_space == -1:
            candidate = source_text[index:]
            return acc + [candidate] if candidate else acc
        else:
            candidate = source_text[index:next_space]
            updated_acc = acc + [candidate] if candidate else acc
            return extract_valid_terms(source_text, next_space + 1, updated_acc)

    raw_items: List[str] = extract_valid_terms(alphanumeric_sequence, 0, [])

    def quicksort(collection: List[str]) -> List[str]:
        if len(collection) <= 1:
            return collection
        pivot = collection[0]
        less_than = [item for item in collection[1:] if digit_values[item] < digit_values[pivot]]
        greater_eq = [item for item in collection[1:] if not (digit_values[item] < digit_values[pivot])]
        return quicksort(less_than) + [pivot] + quicksort(greater_eq)

    ordered_items: List[str] = quicksort(raw_items)

    def concatenate_words(words_list: List[str], idx: int, acc_str: str) -> str:
        if idx == len(words_list):
            return acc_str
        delimiter = '' if idx == 0 else ' '
        return concatenate_words(words_list, idx + 1, acc_str + delimiter + words_list[idx])

    return concatenate_words(ordered_items, 0, '')