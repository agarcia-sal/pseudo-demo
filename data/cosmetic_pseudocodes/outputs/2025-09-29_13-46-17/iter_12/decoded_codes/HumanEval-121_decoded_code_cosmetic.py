from typing import List

def solution(list_of_integers: List[int]) -> int:
    ϕ₈₇: int = 0
    λₐ𝛉: int = 0
    while λₐ𝛉 < len(list_of_integers):
        if λₐ𝛉 % 2 != 1:
            if list_of_integers[λₐ𝛉] % 2 != 0:
                ϕ₈₇ += list_of_integers[λₐ𝛉]
        λₐ𝛉 += 1
    return ϕ₈₇