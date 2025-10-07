from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    # Split string_s by spaces, filter out empty strings
    word_array = list(filter(lambda x: x, map(lambda x: x, string_s.split(" "))))
    iterate_words(word_array, 0, natural_number_n, output_list)
    return output_list


def iterate_words(word_set: List[str], pos_i: int, target_count: int, acc_list: List[str]) -> None:
    if pos_i >= len(word_set):
        return
    count_consonants(word_set[pos_i], 0, 0, target_count, acc_list)
    iterate_words(word_set, pos_i + 1, target_count, acc_list)


def count_consonants(
    text_str: str,
    current_j: int,
    count_c: int,
    limit_n: int,
    collected: List[str],
) -> None:
    if current_j >= len(text_str):
        if count_c == limit_n:
            collected.append(text_str)
        return
    ch = text_str[current_j].lower()
    if ch in ("a", "e", "i", "o", "u"):
        count_consonants(text_str, current_j + 1, count_c, limit_n, collected)
    else:
        count_consonants(text_str, current_j + 1, count_c + 1, limit_n, collected)