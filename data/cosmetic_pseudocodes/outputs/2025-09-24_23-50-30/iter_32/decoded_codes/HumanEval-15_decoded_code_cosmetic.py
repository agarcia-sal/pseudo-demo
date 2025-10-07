from typing import List

def string_sequence(integer_n: int) -> str:
    counter: int = 0
    list_accumulator: List[str] = []
    while counter <= integer_n:
        list_accumulator.append(str(counter))
        counter += 1

    output_string: str = ""
    index_var: int = 0
    if len(list_accumulator) != 0:
        output_string = list_accumulator[0]
        index_var = 1
        while index_var < len(list_accumulator):
            output_string += " " + list_accumulator[index_var]
            index_var += 1

    return output_string