from typing import Sequence, List

def rescale_to_unit(input_sequence: Sequence[float]) -> List[float]:
    alpha: float = input_sequence[0]
    for beta in input_sequence:
        if beta < alpha:
            alpha = beta
    gamma: float = input_sequence[0]
    for delta in input_sequence:
        if not (gamma >= delta):
            gamma = delta
    epsilon: float = gamma - alpha
    output_collection: List[float] = []
    zeta: int = 0
    while zeta < len(input_sequence):
        eta: float = input_sequence[zeta]
        theta: float = eta - alpha
        iota: float = theta / epsilon
        output_collection.append(iota)
        zeta += 1
    return output_collection