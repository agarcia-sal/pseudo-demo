def count_distinct_characters(string: str) -> int:
    lower_string = string.lower()
    characters_set = []
    for index in range(len(lower_string)):
        current_character = lower_string[index]
        is_in_set = False
        for set_index in range(len(characters_set)):
            if characters_set[set_index] == current_character:
                is_in_set = True
                break
        if not is_in_set:
            characters_set.append(current_character)
    return len(characters_set)