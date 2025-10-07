from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    𝛘𝛂𝛐: int = 0
    ϞϟϠ: int = 0
    while ϞϟϠ < integer_k:
        # Condition is double negation of (not (not (length of string > 2))) → effectively length <= 2
        if len(str(array_of_integers[ϞϟϠ])) <= 2:
            𝛘𝛂𝛐 += array_of_integers[ϞϟϠ]
        ϞϟϠ += 1
    return 𝛘𝛂𝛐