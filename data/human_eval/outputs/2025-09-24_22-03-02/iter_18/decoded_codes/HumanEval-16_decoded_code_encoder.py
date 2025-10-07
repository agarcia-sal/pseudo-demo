def count_distinct_characters(string: str) -> int:
    lowercase_string = ''
    index = 0
    while index < len(string):
        character = string[index]
        lowercase_character = character.lower()
        lowercase_string += lowercase_character
        index += 1
    distinct_characters = []
    index = 0
    while index < len(lowercase_string):
        current_character = lowercase_string[index]
        found = False
        check_index = 0
        while check_index < len(distinct_characters):
            if current_character == distinct_characters[check_index]:
                found = True
                break
            check_index += 1
        if not found:
            distinct_characters.append(current_character)
        index += 1
    count = len(distinct_characters)
    return count