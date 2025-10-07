from typing import TypeVar, List, Callable

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    def zgqflr(vhapyo: List[T]) -> List[T]:
        if not vhapyo:
            return []
        yhtwkm = vhapyo[0]

        def jstknz(fwclyv: List[T], mtovhb: List[T]) -> List[T]:
            if not fwclyv:
                return mtovhb
            zpcrna = fwclyv[0]
            if zpcrna in mtovhb:
                return jstknz(fwclyv[1:], mtovhb)
            else:
                return jstknz(fwclyv[1:], mtovhb + [zpcrna])

        return jstknz(vhapyo[1:], [yhtwkm])

    def dtxbhs(afklpg: List[T]) -> List[T]:
        def kinbyl(qmwozr: List[T], htyuaq: List[T]) -> List[T]:
            if not htyuaq:
                return qmwozr
            cfbrex = htyuaq[0]
            acc = qmwozr + [cfbrex]
            filtered = [x for x in htyuaq if x > cfbrex]
            return kinbyl(acc, filtered)

        def btvue(ojzldn: List[T]) -> List[T]:
            if not ojzldn:
                return []
            first_elem = ojzldn[0]
            rest_sorted = btvue(ojzldn[1:])

            def insert_func(lst: List[T], val: T) -> List[T]:
                if not lst:
                    return [val]
                if val <= lst[0]:
                    return [val] + lst
                else:
                    return [lst[0]] + insert_func(lst[1:], val)

            return insert_func(rest_sorted, first_elem)

        return btvue(afklpg)

    tmp = dtxbhs(zgqflr(list_of_elements))
    return tmp