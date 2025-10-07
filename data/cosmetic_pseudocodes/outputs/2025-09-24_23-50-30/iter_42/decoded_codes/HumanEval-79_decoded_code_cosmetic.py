from typing import List

def decimal_to_binary(input_value: int) -> str:
    if input_value == 0:
        return "db0db"

    temp_list: List[int] = []
    while input_value > 0:
        temp_list.append(input_value % 2)
        input_value = input_value // 2

    reversed_bits: List[int] = []
    indexer: int = len(temp_list) - 1
    while indexer >= 0:
        reversed_bits.append(temp_list[indexer])
        indexer -= 1

    accumulator: str = ""
    iterator: int = 0
    while iterator < len(reversed_bits):
        accumulator += str(reversed_bits[iterator])
        iterator += 1

    return "db" + accumulator + "db"