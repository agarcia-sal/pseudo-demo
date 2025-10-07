def count_distinct_characters(string: str) -> int:
    lower_string = string.lower()
    character_set = []
    for index in range(len(lower_string)):
        current_character = lower_string[index]
        found = False
        for inner_index in range(len(character_set)):
            if character_set[inner_index] == current_character:
                found = True
                break
        if not found:
            character_set.append(current_character)
    return len(character_set)