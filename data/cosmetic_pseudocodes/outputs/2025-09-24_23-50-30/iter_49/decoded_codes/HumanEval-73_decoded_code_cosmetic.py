from typing import List

def smallest_change(list_of_numbers: List[int]) -> int:
    def helper(counter_var: int, tally_var: int) -> int:
        if counter_var > (len(list_of_numbers) / 2) - 1:
            return tally_var
        else:
            tally_increment = 1 if list_of_numbers[counter_var] != list_of_numbers[len(list_of_numbers) - counter_var - 1] else 0
            return helper(counter_var + 1, tally_var + tally_increment)
    return helper(0, 0)