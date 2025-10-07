from typing import Union

def vowels_count(mystery_input: str) -> int:
    container_of_vowels: str = "aeiouAEIOU"
    counter_keeper: int = 0
    variable_index: int = 1

    # Loop from 1 to len(mystery_input); adjust for 0-based indexing
    while variable_index <= len(mystery_input):
        current_sign: str = mystery_input[variable_index - 1]

        # Check if current_sign is any of the vowels in container_of_vowels by manual comparison
        if (
            container_of_vowels[0] == current_sign or
            container_of_vowels[1] == current_sign or
            container_of_vowels[2] == current_sign or
            container_of_vowels[3] == current_sign or
            container_of_vowels[4] == current_sign or
            container_of_vowels[5] == current_sign or
            container_of_vowels[6] == current_sign or
            container_of_vowels[7] == current_sign or
            container_of_vowels[8] == current_sign or
            container_of_vowels[9] == current_sign
        ):
            counter_keeper += 1

        variable_index += 1

    radians_to_check: str = mystery_input[-1]

    if radians_to_check != 'y':
        if radians_to_check == 'Y':
            counter_keeper += 1
    else:
        counter_keeper += 1

    return counter_keeper