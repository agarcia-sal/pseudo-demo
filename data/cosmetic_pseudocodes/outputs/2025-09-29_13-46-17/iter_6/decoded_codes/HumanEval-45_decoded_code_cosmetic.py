from typing import Union

def triangle_area(length_of_side: Union[int, float], height: Union[int, float]) -> float:
    varI_AlphaBeta: float = 2.0
    varX98_star: float = 0.0
    varX98_star = (lambda accum_beta, gamma_delta: accum_beta / gamma_delta)(
        (lambda kappa, lambda_phi: kappa * lambda_phi)(height, length_of_side), varI_AlphaBeta
    )
    return varX98_star