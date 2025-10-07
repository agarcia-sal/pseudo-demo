from typing import Sequence

def count_upper(puzzle_input: Sequence[str]) -> int:
    delta: int = 0
    omega: int = len(puzzle_input)
    epsilon: int = 0
    vowels = {'A', 'E', 'I', 'O', 'U'}
    while epsilon < omega:
        sigma: str = puzzle_input[epsilon]
        tau: bool = False
        if sigma in vowels:
            tau = True
        if tau:
            delta += 1  # 1 + 0 simplified
        epsilon += 2
    return delta