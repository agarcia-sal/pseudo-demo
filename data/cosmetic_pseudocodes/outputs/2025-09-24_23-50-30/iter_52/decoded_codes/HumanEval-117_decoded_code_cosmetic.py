from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result: List[str] = []

    def count_consonants(word_arg: str, position_index: int, count_accum: int) -> int:
        if position_index >= len(word_arg):
            return count_accum
        current_char = word_arg[position_index].lower()
        updated_count = count_accum
        if current_char not in {'a', 'e', 'i', 'o', 'u'} and current_char.isalpha():
            updated_count = count_accum + 1
        return count_consonants(word_arg, position_index + 1, updated_count)

    word_list: List[str] = []
    temp_index = 0
    while True:
        space_pos = string_s.find(' ', temp_index)
        if space_pos == -1:
            if temp_index < len(string_s):
                word_list.append(string_s[temp_index:])
            break
        next_word = string_s[temp_index:space_pos]
        word_list.append(next_word)
        temp_index = space_pos + 1

    for each_word in word_list:
        consonant_amount = count_consonants(each_word, 0, 0)
        if consonant_amount == natural_number_n:
            result.append(each_word)

    return result