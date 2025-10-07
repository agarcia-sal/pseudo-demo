def count_distinct_characters(string: str) -> int:
    lowercase_string = ""
    index = 0
    while index < len(string):
        current_character = string[index]
        lowercase_character = current_character.lower()
        lowercase_string += lowercase_character
        index += 1
    distinct_characters = []
    index = 0
    while index < len(lowercase_string):
        current_character = lowercase_string[index]
        is_in_list = False
        check_index = 0
        while check_index < len(distinct_characters):
            if current_character == distinct_characters[check_index]:
                is_in_list = True
                break
            check_index += 1
        if not is_in_list:
            distinct_characters.append(current_character)
        index += 1
    result = len(distinct_characters)
    return result