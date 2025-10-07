def count_distinct_characters(string: str) -> int:
    lowercase_string = string.lower()
    character_set = []
    for index in range(len(lowercase_string)):
        current_character = lowercase_string[index]
        is_in_set = False
        for set_index in range(len(character_set)):
            if character_set[set_index] == current_character:
                is_in_set = True
                break
        if not is_in_set:
            character_set.append(current_character)
    return len(character_set)