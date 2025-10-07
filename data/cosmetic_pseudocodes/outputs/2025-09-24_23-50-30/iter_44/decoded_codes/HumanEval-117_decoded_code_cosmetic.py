from typing import List


def select_words(parameter_alpha: str, parameter_beta: int) -> List[str]:
    accumulator: List[str] = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for element in parameter_alpha.split(" "):
        counter_var = 0
        for counter_var_2 in range(len(element)):
            if element[counter_var_2].lower() not in vowels:
                counter_var += 1
        if counter_var == parameter_beta:
            accumulator.append(element)
    return accumulator