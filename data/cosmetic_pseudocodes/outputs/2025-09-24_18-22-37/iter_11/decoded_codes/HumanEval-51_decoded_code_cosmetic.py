def remove_vowels(input_string: str) -> str:
    result_string = ""
    index_counter = 0
    vowels = {"a", "e", "i", "o", "u"}

    while index_counter < len(input_string):
        current_char = input_string[index_counter]
        lower_char = current_char.lower()
        vowel_check = lower_char in vowels
        if not vowel_check:
            result_string += current_char
        index_counter += 1

    return result_string