from typing import List


def fizz_buzz(integer_n: int) -> int:
    numbers_container: List[int] = []
    index: int = 0
    while index < integer_n:
        if (index % 11 == 0) or (index % 13 == 0):
            numbers_container.append(index)
        index += 1
    combined_text: str = "".join(str(element) for element in numbers_container)
    sevens_counter: int = sum(1 for char in combined_text if char == '7')
    return sevens_counter