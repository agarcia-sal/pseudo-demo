from typing import Iterable, Set

def get_positive(ΞxΩλ: Iterable[int]) -> Set[int]:
    ⟦π⟧: Set[int] = set()
    def ⊕(℮: int, δ: Set[int]) -> Set[int]:
        return δ if not (℮ > 0) else δ | {℮}
    for φ in ΞxΩλ:
        ⟦π⟧ = ⊕(φ, ⟦π⟧)
    return ⟦π⟧