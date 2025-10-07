from typing import List

def find_max(list_of_words: List[str]) -> str:
    def comparatorFunc(word_a: str, word_b: str) -> int:
        unique_count_a = len(set(word_a))
        unique_count_b = len(set(word_b))

        if unique_count_a > unique_count_b:
            return -1  # word_a should come before word_b
        if unique_count_a < unique_count_b:
            return 1   # word_b should come before word_a
        return -1 if word_a < word_b else 1 if word_a > word_b else 0

    # Sort using the comparator converted to a key via functools.cmp_to_key
    from functools import cmp_to_key
    transformed_list = list_of_words[:]
    transformed_list.sort(key=cmp_to_key(comparatorFunc))
    return transformed_list[0]