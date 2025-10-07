from typing import Iterable

def vowels_count(parameter_alpha: str) -> int:
    reference_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    accumulator = sum(1 for element_beta in parameter_alpha if element_beta in reference_set)
    if parameter_alpha and parameter_alpha[-1] in {'Y', 'y'}:
        accumulator += 1
    return accumulator