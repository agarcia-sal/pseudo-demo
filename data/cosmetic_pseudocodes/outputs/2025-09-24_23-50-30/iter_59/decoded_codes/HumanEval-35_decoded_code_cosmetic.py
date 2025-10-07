from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(aa: Sequence[T]) -> T:
    def ab(ac: T, ad: T, ae: T) -> T:
        if not (ae > ad):
            return ad
        else:
            return ae

    af = aa[0]
    ag = 1
    while ag < len(aa):
        af = ab(af, af, aa[ag])
        ag += 1
    return af