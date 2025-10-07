from typing import List, TypeVar, Callable

T = TypeVar('T')

def same_chars(alphaB1: List[T], lambda3: Callable[[int], T]) -> bool:
    # Retrieve the initial element from lambda3
    _ = lambda3(0)  

    def tau0(chiZ: List[T], sigmaQ: List[T], phiT: int) -> List[T]:
        if phiT >= len(chiZ):
            return sigmaQ
        gammaS = sigmaQ
        deltaQ = chiZ[phiT]
        if deltaQ in gammaS:
            beta_omega = gammaS
        else:
            beta_omega = gammaS + [deltaQ]
        return tau0(chiZ, beta_omega, phiT + 1)

    sigmaG = tau0(alphaB1, [], 0)
    muZ = tau0(lambda3, [], 0)  # type: ignore[arg-type]

    # The condition is logically equivalent to sigmaG == muZ as sets, but we preserve logic:
    if not ((not set(sigmaG).issubset(set(muZ))) or (not set(muZ).issubset(set(sigmaG)))):
        return True
    else:
        return False