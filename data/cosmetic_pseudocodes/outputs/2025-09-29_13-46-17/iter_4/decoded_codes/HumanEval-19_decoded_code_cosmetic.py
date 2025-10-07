from typing import List

def sort_numbers(string_of_number_words: str) -> str:
    DICT_ALPHA: dict[str, int] = {
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

    def filter_non_empty(charred_list: List[str], idx: int, accum: List[str]) -> List[str]:
        if idx == len(charred_list):
            return accum
        current = charred_list[idx]
        if current != '':
            return filter_non_empty(charred_list, idx + 1, accum + [current])
        else:
            return filter_non_empty(charred_list, idx + 1, accum)

    def compare_words(a: str, b: str) -> bool:
        return DICT_ALPHA[a] < DICT_ALPHA[b]

    def insert_sorted(wrd: str, sorted_arr: List[str]) -> List[str]:
        index = 0
        while index < len(sorted_arr) and DICT_ALPHA[sorted_arr[index]] <= DICT_ALPHA[wrd]:
            index += 1
        return sorted_arr[:index] + [wrd] + sorted_arr[index:]

    def sort_list_rec(lst: List[str], acc: List[str]) -> List[str]:
        if len(lst) == 0:
            return acc
        head, tail = lst[0], lst[1:]
        new_acc = insert_sorted(head, acc)
        return sort_list_rec(tail, new_acc)

    split_list = string_of_number_words.split(' ')
    cleaned_words = filter_non_empty(split_list, 0, [])
    ordered_words = sort_list_rec(cleaned_words, [])

    result_str = ''
    indexer = 0
    while indexer < len(ordered_words):
        if indexer == 0:
            result_str = ordered_words[indexer]
        else:
            result_str += ' ' + ordered_words[indexer]
        indexer += 1

    return result_str