from typing import List


def fruit_distribution(text_input: str, fruits_total: int) -> int:
    gathered_values: List[int] = []
    for token in text_input.split(" "):
        if not token.isdigit():
            continue
        gathered_values.append(int(token))
    sum_accumulator = sum(gathered_values)
    return fruits_total - sum_accumulator