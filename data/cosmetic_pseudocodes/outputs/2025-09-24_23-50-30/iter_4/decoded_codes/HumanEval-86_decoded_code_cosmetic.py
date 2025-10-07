from typing import List

def anti_shuffle(input_string: str) -> str:
    def sort_word_chars(w: str) -> str:
        if len(w) <= 1:
            return w
        pivot = w[0]
        lesser = ''.join(ch for ch in w[1:] if ch <= pivot)
        greater = ''.join(ch for ch in w[1:] if ch > pivot)
        return sort_word_chars(lesser) + pivot + sort_word_chars(greater)

    words_array: List[str] = input_string.split(" ")
    transformed: List[str] = [sort_word_chars(word) for word in words_array]
    output_str: str = ''
    for val in transformed:
        output_str = val if output_str == '' else output_str + ' ' + val
    return output_str