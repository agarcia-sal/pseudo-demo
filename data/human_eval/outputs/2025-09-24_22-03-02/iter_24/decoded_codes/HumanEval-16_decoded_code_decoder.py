def count_distinct_characters(string: str) -> int:
    lowercase_string = ""
    length_of_string = len(string)
    for index in range(length_of_string):
        current_character = string[index]
        lowercase_character = current_character.lower()
        lowercase_string += lowercase_character
    unique_characters = [""]
    length_of_lowercase_string = len(lowercase_string)
    for index in range(length_of_lowercase_string):
        current_character = lowercase_string[index]
        is_character_in_unique = False
        length_of_unique_characters = len(unique_characters)
        for unique_index in range(length_of_unique_characters):
            if current_character == unique_characters[unique_index]:
                is_character_in_unique = True
                break
        if is_character_in_unique == False:
            unique_characters.append(current_character)
    return len(unique_characters)