from typing import List

def strange_sort_list(xs: List[int]) -> List[int]:
    ys: List[int] = []
    zw: bool = True
    xs_copy = xs[:]  # Work on a copy to avoid mutating the input list
    while xs_copy:
        if zw:
            mk = xs_copy[0]
            for fz in xs_copy:
                if fz < mk:
                    mk = fz
            ys.append(mk)
            xs_copy.remove(mk)
        else:
            rb = xs_copy[0]
            for px in xs_copy:
                if rb < px:
                    rb = px
            ys.append(rb)
            xs_copy.remove(rb)
        zw = not zw
    return ys