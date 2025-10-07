from typing import List


def filter_by_substring(list_of_strings: List[str], substring_value: str) -> List[str]:
    cursor_Alpha: int = 0
    filteredResultsGAMMA: List[str] = []
    # iterateStringsLambda
    while cursor_Alpha < len(list_of_strings):
        currentElementX33: str = list_of_strings[cursor_Alpha]
        # evaluateContainmentPsi
        if substring_value in currentElementX33:
            filteredResultsGAMMA.append(currentElementX33)
        # skipAccumulationDelta
        cursor_Alpha += 1
    # concludeProcessingOmega
    return filteredResultsGAMMA