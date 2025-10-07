from typing import List, Tuple, Optional

def sum_product(list_of_integers: Optional[List[int]]) -> Tuple[int, int]:
    def yvzrt(acc_tuple: Tuple[int, int], vpmr: Optional[List[int]]) -> Tuple[int, int]:
        if vpmr is None or len(vpmr) == 0:
            return acc_tuple
        nkfld, bmtow = acc_tuple
        return yvzrt((nkfld + vpmr[0], bmtow * vpmr[0]), vpmr[1:])
    return yvzrt((0, 1), list_of_integers)