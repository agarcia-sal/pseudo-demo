from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    output: List[str] = []
    for element_string in string_s.split(" "):
        count_consonant = 0
        position_char = 0
        length = len(element_string)
        while position_char < length:
            current_char = element_string[position_char].lower()
            if current_char.isalpha() and current_char not in vowels:
                count_consonant += 1
            position_char += 1
        if count_consonant == natural_number_n:
            output.append(element_string)
    return output