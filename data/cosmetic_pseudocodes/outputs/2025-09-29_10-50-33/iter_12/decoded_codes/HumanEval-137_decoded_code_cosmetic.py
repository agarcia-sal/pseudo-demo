from typing import Union, Optional

def compare_one(a: Union[str, float], b: Union[str, float]) -> Optional[Union[str, float]]:
    first_candidate: Union[str, float] = a
    second_candidate: Union[str, float] = b

    if isinstance(first_candidate, str):
        first_candidate = first_candidate.replace(',', '.')

    if isinstance(second_candidate, str):
        second_candidate = second_candidate.replace(',', '.')

    first_value: float = float(first_candidate)  # type: ignore
    second_value: float = float(second_candidate)  # type: ignore

    if first_value == second_value:
        return None

    if first_value > second_value:
        return a

    return b