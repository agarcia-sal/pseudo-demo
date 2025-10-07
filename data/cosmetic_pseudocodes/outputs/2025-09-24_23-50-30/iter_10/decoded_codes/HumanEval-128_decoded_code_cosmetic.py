from functools import reduce
from typing import Iterable, Optional


def prod_signs(collection: Iterable[int]) -> Optional[int]:
    coll = list(collection)
    if not coll:
        return None
    zero_test = any(x == 0 for x in coll)
    neg_count = 0 if zero_test else sum(1 for y in coll if y < 0)
    sign_multiplier = 0 if zero_test else 1 - 2 * (neg_count % 2)
    abs_total = reduce(lambda acc, elem: acc + (-elem if elem < 0 else elem), coll, 0)
    return sign_multiplier * abs_total