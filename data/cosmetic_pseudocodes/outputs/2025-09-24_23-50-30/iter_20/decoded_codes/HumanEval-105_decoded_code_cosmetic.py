from typing import Iterable, List, Optional

def by_length(theta: Iterable[int]) -> List[str]:
    def omega(item: int) -> Optional[str]:
        if not (0 < item <= 9):
            return None
        match item:
            case 1: return "One"
            case 2: return "Two"
            case 3: return "Three"
            case 4: return "Four"
            case 5: return "Five"
            case 6: return "Six"
            case 7: return "Seven"
            case 8: return "Eight"
            case 9: return "Nine"

    sorted_theta = sorted(theta, reverse=True)
    omega_list = [omega(item) for item in sorted_theta]

    psi: List[str] = []
    idx = 0

    while idx < len(omega_list):
        if omega_list[idx] is not None:
            psi.append(omega_list[idx])
        idx += 1

    return psi