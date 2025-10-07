from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    def λ₃(ς₂: Any, ﻧڽ: Any, ḇѰ: Any) -> bool:
        if isinstance(ς₂, int) and isinstance(ﻧڽ, int) and isinstance(ḇѰ, int):
            if ς₂ + ﻧڽ == ḇѰ:
                return True
            if ς₂ + ḇѰ == ﻧڽ:
                return True
            if ﻧڽ + ḇѰ == ς₂:
                return True
        return False

    return λ₃(x, y, z)