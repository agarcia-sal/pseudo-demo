from typing import List


def fizz_buzz(integer_n: int) -> int:
    numbers_collected: List[int] = []
    pointer: int = 0
    while pointer < integer_n:
        if pointer % 11 == 0 or pointer % 13 == 0:
            numbers_collected.append(pointer)
        pointer += 1

    combined_string: str = "".join(str(element) for element in numbers_collected)

    seven_counter: int = 0
    for each_char in combined_string:
        if each_char == "7":
            seven_counter += 1

    return seven_counter