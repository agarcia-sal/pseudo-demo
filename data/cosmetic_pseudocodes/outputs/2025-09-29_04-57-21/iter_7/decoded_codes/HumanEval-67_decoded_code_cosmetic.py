from typing import List, Iterator, Optional


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    extracted_numbers: List[int] = []
    parts_iterator: Iterator[str] = iter(string_description.split(' '))
    while True:
        current_token: Optional[str]
        try:
            current_token = next(parts_iterator)
        except StopIteration:
            current_token = None
        if current_token is None:
            break
        if current_token.isdigit():
            extracted_numbers.append(int(current_token))

    accumulated_sum: int = 0
    idx: int = 0
    while idx < len(extracted_numbers):
        accumulated_sum += extracted_numbers[idx]
        idx += 1

    return total_number_of_fruits - accumulated_sum