from typing import Dict

def count_distinct_characters(beta: str) -> int:
    delta: Dict[str, bool] = {}
    eta: int = 0
    for gamma in beta.lower():
        if gamma not in delta:
            delta[gamma] = True
            eta += 1
    return eta