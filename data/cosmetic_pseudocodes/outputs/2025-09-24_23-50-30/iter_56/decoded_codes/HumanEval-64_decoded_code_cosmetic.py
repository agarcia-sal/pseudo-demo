from typing import Union


def vowels_count(parameter_alpha: str) -> int:
    variable_bravo: str = "AEIOUaeiou"
    variable_charlie: int = 0
    variable_delta: int = 0
    variable_echo: int = len(parameter_alpha)
    while variable_delta < variable_echo:
        variable_foxtrot: str = parameter_alpha[variable_delta : variable_delta + 1]
        variable_charlie += 1 if variable_foxtrot in variable_bravo else 0
        variable_delta += 1
    if variable_echo > 0 and parameter_alpha[variable_echo - 1] in ('y', 'Y'):
        variable_charlie += 1
    return variable_charlie