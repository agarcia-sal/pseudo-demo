def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_characters = []
    text_length = len(text)
    index = 0
    while index < text_length:
        current_character = text[index]
        current_character_lower = current_character.lower()
        is_vowel = False
        vowel_index = 0
        vowels_length = len(vowels)
        while vowel_index < vowels_length:
            if current_character_lower == vowels[vowel_index]:
                is_vowel = True
                break
            vowel_index += 1
        if is_vowel == False:
            result_characters.append(current_character)
        index += 1
    result_string = ""
    result_length = len(result_characters)
    result_index = 0
    while result_index < result_length:
        result_string += result_characters[result_index]
        result_index += 1
    return result_string