def flip_case(input_string: str) -> str:
    result_string = []
    for character in input_string:
        if character.islower():
            result_string.append(character.upper())
        elif character.isupper():
            result_string.append(character.lower())
        else:
            result_string.append(character)
    return ''.join(result_string)