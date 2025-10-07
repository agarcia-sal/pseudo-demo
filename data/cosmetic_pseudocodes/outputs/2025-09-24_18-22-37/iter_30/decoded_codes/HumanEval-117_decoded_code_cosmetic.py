from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    collected: List[str] = []
    terms: List[str] = string_s.split(" ")
    term_cursor: int = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    while term_cursor < len(terms):
        current_term = terms[term_cursor]
        consonant_count = 0
        char_index = 0

        # Iterate through characters of current_term except the last one
        while char_index < len(current_term) - 1:
            the_letter = current_term[char_index].lower()
            if the_letter in vowels:
                break
            consonant_count += 1
            char_index += 1
        else:
            # Only executed if the while loop wasn't broken: 
            # meaning no vowel found before last char
            char_index = len(current_term) - 1

        if consonant_count != natural_number_n:
            term_cursor += 1
            continue

        collected.append(current_term)
        term_cursor += 1

    return collected