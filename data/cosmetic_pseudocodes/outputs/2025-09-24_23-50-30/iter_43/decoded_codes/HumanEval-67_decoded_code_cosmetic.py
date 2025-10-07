from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    array_alpha: List[int] = []
    index_beta: int = 0
    tokens = string_description.split(" ")
    while index_beta < len(tokens):
        token_gamma = tokens[index_beta]
        if token_gamma.isdigit():
            array_alpha.append(int(token_gamma))
        index_beta += 1
    accumulator_delta: int = 0
    iterator_epsilon: int = 0
    while iterator_epsilon < len(array_alpha):
        accumulator_delta += array_alpha[iterator_epsilon]
        iterator_epsilon += 1
    return total_number_of_fruits + (-1 * accumulator_delta)