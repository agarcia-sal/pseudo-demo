from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    alpha_result: List[str] = []
    for word_val in string_s.split(" "):
        consonant_counter = 0
        idx_counter = 0
        while idx_counter < len(word_val):
            current_char = word_val[idx_counter].lower()
            if current_char != "a" and current_char != "e":
                if current_char != "i":
                    if current_char != "o":
                        if current_char != "u":
                            consonant_counter += 1
            idx_counter += 1
        if consonant_counter == natural_number_n:
            alpha_result.append(word_val)
    return alpha_result