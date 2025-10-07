from typing import List

def flip_case(parameter_string: str) -> str:
    accumulator: List[str] = []
    for temporary_character in parameter_string:
        if temporary_character.islower():
            accumulator.append(temporary_character.upper())
        elif temporary_character.isupper():
            accumulator.append(temporary_character.lower())
        else:
            accumulator.append(temporary_character)
    return "".join(accumulator)