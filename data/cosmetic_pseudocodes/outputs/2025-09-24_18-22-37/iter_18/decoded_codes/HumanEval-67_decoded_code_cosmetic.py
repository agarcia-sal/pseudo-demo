from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    aggregate_values: List[int] = []
    iterator_index: int = 0
    tokens: List[str] = string_description.split()

    while iterator_index < len(tokens):
        candidate_token: str = tokens[iterator_index]
        iterator_index += 1

        if not candidate_token.isdigit():
            continue

        numeric_value: int = int(candidate_token)
        aggregate_values.append(numeric_value)

    total_accumulated: int = 0
    for index in range(len(aggregate_values)):
        total_accumulated += aggregate_values[index]

    return total_number_of_fruits - total_accumulated