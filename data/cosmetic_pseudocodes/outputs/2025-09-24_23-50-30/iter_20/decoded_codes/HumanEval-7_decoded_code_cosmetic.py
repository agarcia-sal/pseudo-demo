from typing import Iterable, List

def filter_by_substring(alpha_collection: Iterable[str], beta_pattern: str) -> List[str]:
    delta_result: List[str] = []
    for epsilon_text in alpha_collection:
        if beta_pattern in epsilon_text:
            delta_result.append(epsilon_text)
    return delta_result