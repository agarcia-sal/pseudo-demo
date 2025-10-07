def count_distinct_characters(string: str) -> int:
    distinct_characters = []
    index = 0
    while index < len(string):
        character = string[index]
        lower_character = character.lower()
        found = False
        check_index = 0
        while check_index < len(distinct_characters):
            if distinct_characters[check_index] == lower_character:
                found = True
                break
            check_index += 1
        if not found:
            distinct_characters.append(lower_character)
        index += 1
    return len(distinct_characters)