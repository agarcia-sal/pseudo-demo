def words_string(input_string: str) -> list[str]:
    if not input_string:
        return []

    character_list = []
    for character in input_string:
        if character == ',':
            character_list.append(' ')
        else:
            character_list.append(character)

    joined_string = ''.join(character_list)
    return joined_string.split()