def count_distinct_characters(string: str) -> int:
    lowered_string = string.lower()
    characters_set = []
    string_length = len(lowered_string)
    index = 0
    while index < string_length:
        current_character = lowered_string[index]
        found = False
        set_length = len(characters_set)
        set_index = 0
        while set_index < set_length:
            if characters_set[set_index] == current_character:
                found = True
            set_index += 1
        if found == False:
            characters_set.append(current_character)
        index += 1
    result = len(characters_set)
    return result