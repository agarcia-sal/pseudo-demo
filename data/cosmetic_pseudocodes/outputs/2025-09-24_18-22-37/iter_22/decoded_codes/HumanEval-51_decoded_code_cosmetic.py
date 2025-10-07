def remove_vowels(message: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}
    filtered_result = []
    index_counter = 0
    while index_counter < len(message):
        current_character = message[index_counter]
        if current_character.lower() not in vowels:
            filtered_result.append(current_character)
        index_counter += 1
    return "".join(filtered_result)