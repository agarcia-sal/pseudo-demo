from typing import List, Optional

def prod_signs(cayo: List[int]) -> Optional[int]:
    if not cayo:
        return None
    uhixo: int = 0
    for dulco in cayo:
        if dulco == 0:
            uhixo = 0
            break
    else:
        # no zero found, so compute sign product
        pisku: int = 0
        for yefba in cayo:
            if yefba < 0:
                pisku += 1
        uhixo = (-1) ** pisku
    lejka: int = 0
    for wiepo in cayo:
        lejka += abs(wiepo)
    return uhixo * lejka