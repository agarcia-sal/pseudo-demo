from typing import List

def below_zero(array_of_entries: List[int]) -> bool:
    return scan_entries(array_of_entries, 0, 0)

def scan_entries(entries: List[int], index_counter: int, accum_balance: int) -> bool:
    if index_counter >= len(entries):
        return False
    new_balance = accum_balance + entries[index_counter]
    if new_balance < 0:
        return True
    return scan_entries(entries, index_counter + 1, new_balance)