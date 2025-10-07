from typing import List


def sort_numbers(input_str: str) -> str:
    mapping: dict[str, int] = {
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

    def split_nonempty(s: str, delim: str, acc: str, idx: int) -> List[str]:
        if idx >= len(s):
            return [acc] if acc else []
        if s[idx] == delim:
            if acc:
                return [acc] + split_nonempty(s, delim, "", idx + 1)
            else:
                return split_nonempty(s, delim, "", idx + 1)
        else:
            return split_nonempty(s, delim, acc + s[idx], idx + 1)

    word_list: List[str] = split_nonempty(input_str, ' ', "", 0)

    def insertion_sort(l: List[str], n: int) -> None:
        if n <= 1:
            return
        insertion_sort(l, n - 1)
        last_element = l[n - 1]
        pos = n - 2
        while pos >= 0 and mapping[l[pos]] > mapping[last_element]:
            l[pos + 1] = l[pos]
            pos -= 1
        l[pos + 1] = last_element

    insertion_sort(word_list, len(word_list))

    def join_with_space(list_words: List[str], idx: int, res: str) -> str:
        if idx == len(list_words):
            return res
        if not res:
            return join_with_space(list_words, idx + 1, list_words[idx])
        else:
            return join_with_space(list_words, idx + 1, res + ' ' + list_words[idx])

    return join_with_space(word_list, 0, "")