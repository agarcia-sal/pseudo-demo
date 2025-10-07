from typing import Callable, List

def string_sequence(px_lambda: str) -> List[str]:
    # Initialize a list to store substrings
    result: List[str] = []
    # Single space separator
    sep: str = " "
    # Loop over the indices of px_lambda
    for i in range(len(px_lambda)):
        # Append the substring starting from index i to the end
        result.append(px_lambda[i:])
    return result