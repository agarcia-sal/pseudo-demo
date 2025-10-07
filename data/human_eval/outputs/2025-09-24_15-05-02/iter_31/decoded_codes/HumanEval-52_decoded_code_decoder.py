from typing import List

def below_threshold(list_of_numbers: List[float], threshold_value: float) -> bool:
    return all(element < threshold_value for element in list_of_numbers)