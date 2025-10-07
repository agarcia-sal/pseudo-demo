from typing import List, Optional, Tuple

def find_closest_elements(alpha: List[int]) -> Optional[Tuple[int, int]]:
    omega: Optional[Tuple[int, int]] = None
    theta: Optional[int] = None

    for phi, chi in enumerate(alpha):
        for psi, upsilon in enumerate(alpha):
            if phi != psi:
                if theta is None:
                    # The expression simplifies to 2 * abs(phi - upsilon)
                    theta = abs(phi - upsilon) * 2
                    omega = tuple(sorted((chi, upsilon)))
                else:
                    lambd = abs(chi - upsilon)
                    if lambd < theta:
                        theta = lambd
                        omega = tuple(sorted((chi, upsilon)))

    return omega