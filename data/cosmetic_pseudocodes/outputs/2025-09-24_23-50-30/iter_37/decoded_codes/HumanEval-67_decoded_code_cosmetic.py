from functools import reduce
from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    bag: List[int] = []
    for part in string_description.split(" "):
        if part.isdigit():
            bag.append(int(part))
    return total_number_of_fruits - sum(bag)