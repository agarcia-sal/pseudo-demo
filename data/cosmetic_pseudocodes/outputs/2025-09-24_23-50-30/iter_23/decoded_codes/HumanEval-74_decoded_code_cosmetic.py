from typing import Sequence, Sized

def total_match(alpha_collection: Sequence[Sized], beta_collection: Sequence[Sized]) -> Sequence[Sized]:
    total_alpha: int = 0
    total_beta: int = 0
    for index in range(len(alpha_collection)):
        total_alpha += len(alpha_collection[index])
    for position in range(len(beta_collection)):
        total_beta += len(beta_collection[position])
    if not (total_alpha > total_beta):
        return alpha_collection
    return beta_collection