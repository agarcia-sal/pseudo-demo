def remove_vowels(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result_characters = []
    index = 0
    while index < len(text):
        current_character = text[index]
        current_character_lower = current_character.lower()
        is_vowel = False
        vowel_index = 0
        while vowel_index < len(vowels):
            if current_character_lower == vowels[vowel_index]:
                is_vowel = True
                break
            vowel_index += 1
        if not is_vowel:
            result_characters.append(current_character)
        index += 1
    result_string = ""
    result_index = 0
    while result_index < len(result_characters):
        result_string += result_characters[result_index]
        result_index += 1
    return result_string