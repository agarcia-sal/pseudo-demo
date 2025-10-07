from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    fruit_counts: List[int] = []
    for token in string_description.split(' '):
        if token.isdigit():
            fruit_counts.append(int(token))
    consumed_fruits = sum(fruit_counts)
    return total_number_of_fruits - consumed_fruits