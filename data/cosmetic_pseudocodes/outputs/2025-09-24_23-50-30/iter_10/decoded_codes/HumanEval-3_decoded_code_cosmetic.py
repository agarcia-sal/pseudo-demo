from typing import List

def below_zero(list_of_operations: List[int]) -> bool:
    accumulator: int = 0

    while True:
        if not list_of_operations:
            return False

        current_item: int = list_of_operations[0]
        list_of_operations = list_of_operations[1:]

        accumulator += current_item

        if accumulator < 0:
            return True