from typing import List


def fizz_buzz(parameter_x: int) -> int:
    collection_a: List[int] = []

    def add_element(value_z: int) -> None:
        collection_a.append(value_z)

    def process_index(index_y: int) -> None:
        if (index_y % 11 == 0 or index_y % 13 == 0):
            add_element(index_y)

    def iterate_counter(counter_v: int) -> None:
        if counter_v < parameter_x:
            process_index(counter_v)
            iterate_counter(counter_v + 1)

    iterate_counter(0)

    string_b: str = ""

    def append_elements(pos_w: int) -> None:
        nonlocal string_b
        if pos_w < len(collection_a):
            string_b += str(collection_a[pos_w])
            append_elements(pos_w + 1)

    append_elements(0)

    counter_c: int = 0

    def tally_chars(pos_d: int) -> None:
        nonlocal counter_c
        if pos_d < len(string_b):
            if string_b[pos_d] == "7":
                counter_c += 1
            tally_chars(pos_d + 1)

    tally_chars(0)

    return counter_c