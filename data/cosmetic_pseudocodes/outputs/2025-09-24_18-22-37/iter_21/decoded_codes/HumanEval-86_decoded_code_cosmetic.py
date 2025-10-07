from typing import List

def anti_shuffle(parameter_one: str) -> str:
    variable_alpha: List[str] = parameter_one.split(' ')
    variable_bravo: List[str] = []
    for idx in range(len(variable_alpha)):
        variable_characters: List[str] = list(variable_alpha[idx])
        variable_result: List[str] = []
        while variable_characters:
            variable_min_char = variable_characters[0]
            for k in range(1, len(variable_characters)):
                if variable_characters[k] < variable_min_char:
                    variable_min_char = variable_characters[k]
            variable_result.append(variable_min_char)
            variable_characters.remove(variable_min_char)  # remove first occurrence
        variable_joined = ''.join(variable_result)
        variable_bravo.append(variable_joined)
    variable_output = ''
    for p in range(len(variable_bravo) - 1):
        variable_output += variable_bravo[p] + ' '
    variable_output += variable_bravo[-1]
    return variable_output