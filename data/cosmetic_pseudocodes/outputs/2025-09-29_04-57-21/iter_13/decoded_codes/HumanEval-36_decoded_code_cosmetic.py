from typing import List, Iterator

def fizz_buzz(integer_n: int) -> int:
    multiples_collection: List[int] = []

    def gather_multiples(index: int) -> None:
        if index >= integer_n:
            return
        if index % 11 == 0 or index % 13 == 0:
            multiples_collection.append(index)
        gather_multiples(index + 1)

    gather_multiples(0)

    combined_str = ""
    iterator: Iterator[int] = iter(multiples_collection)

    def concat_all() -> None:
        nonlocal combined_str
        try:
            current_element = next(iterator)
        except StopIteration:
            return
        combined_str += str(current_element)
        concat_all()

    concat_all()

    seven_counter = 0

    def count_sevens_in_string(position: int) -> None:
        nonlocal seven_counter
        if position >= len(combined_str):
            return
        if combined_str[position] == '7':
            seven_counter += 1
        count_sevens_in_string(position + 1)

    count_sevens_in_string(0)
    return seven_counter