from typing import List

def derivative(xs: List[int]) -> List[int]:
    # Return a list of index * coefficient for each term starting from index 1
    return [index * coefficient for index, coefficient in enumerate(xs) if index >= 1]