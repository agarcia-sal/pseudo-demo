from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    output_list: List[str] = []
    words = string_s.split(" ")
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for index_word in range(len(words)):
        temp_word = words[index_word]
        consonant_counter = 0
        i = 0
        while i < len(temp_word):
            current_char = temp_word[i].lower()
            if current_char not in vowels:
                consonant_counter += 1
            i += 1
        if consonant_counter == natural_number_n:
            output_list.append(temp_word)
    return output_list