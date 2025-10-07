from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    result_set: List[str] = []

    word_iterator = string_s.split(" ")
    position = 0
    limit = len(word_iterator)
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while position < limit:
        current_word = word_iterator[position]

        count_nonvowels = 0
        char_index = 0
        word_length = len(current_word)
        while char_index <= word_length - 1:
            target_char = current_word[char_index].lower()

            switch_condition = True
            if target_char in vowels:
                switch_condition = False

            if switch_condition is not False:
                count_nonvowels += 1
            char_index += 1

        if count_nonvowels == natural_number_n:
            result_set.append(current_word)
        position += 1

    return result_set