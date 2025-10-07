from math import floor

def iscube(integer_value: int) -> bool:
    n: int = integer_value
    root_candidate: int = floor(n ** (1/3) + 0.5)
    candidate_cube: int = root_candidate * root_candidate * root_candidate
    return candidate_cube == n or candidate_cube == -n