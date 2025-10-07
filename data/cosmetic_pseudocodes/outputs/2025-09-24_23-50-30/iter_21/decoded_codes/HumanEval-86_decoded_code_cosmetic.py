from typing import List


def anti_shuffle(input_string: str) -> str:
    def sort_word(rec_chars: List[str]) -> List[str]:
        if len(rec_chars) < 2:
            return rec_chars
        pivot_char = rec_chars[0]
        lesser_chars: List[str] = []
        greater_chars: List[str] = []
        for idx in range(1, len(rec_chars)):
            if rec_chars[idx] < pivot_char:
                lesser_chars.append(rec_chars[idx])
            else:
                greater_chars.append(rec_chars[idx])
        return sort_word(lesser_chars) + [pivot_char] + sort_word(greater_chars)

    words_queue: List[str] = input_string.split(" ")
    sorted_words_list: List[str] = []

    while words_queue:
        current_word = words_queue.pop(0)
        char_array: List[str] = [current_word[i] for i in range(1, len(current_word))]
        sorted_chars = sort_word(char_array)
        rebuilt_word = "".join(sorted_chars)
        sorted_words_list.append(rebuilt_word)

    output_string = ""
    for index in range(1, len(sorted_words_list) + 1):
        output_string += sorted_words_list[index - 1]
        if index < len(sorted_words_list):
            output_string += " "
    return output_string