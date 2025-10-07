from typing import Union

def vowels_count(parameter_one: Union[str, list[str]]) -> int:
    number_of_vowels_local: int = 0
    local_vowels: str = "aeiouAEIOU"
    index_iterator: int = 0

    while index_iterator < len(parameter_one):
        current_character: str = parameter_one[index_iterator]
        if current_character in local_vowels:
            number_of_vowels_local += 1
        index_iterator += 1

    if len(parameter_one) > 0 and (parameter_one[-1] == 'Y' or parameter_one[-1] == 'y'):
        number_of_vowels_local += 1

    return number_of_vowels_local