def count_distinct_characters(parameter_alpha: str) -> int:
    accumulator_beta: set[str] = set()
    index_gamma: int = 1
    while index_gamma <= len(parameter_alpha):
        character_delta: str = parameter_alpha[index_gamma - 1].lower()
        if character_delta not in accumulator_beta:
            accumulator_beta.add(character_delta)
        index_gamma += 1
    return len(accumulator_beta)