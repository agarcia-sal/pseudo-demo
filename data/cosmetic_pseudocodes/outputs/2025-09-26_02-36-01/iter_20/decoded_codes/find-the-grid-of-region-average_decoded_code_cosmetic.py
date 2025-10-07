from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def _check_region(a: int, b: int) -> bool:
            for _p in range(3):
                for _q in range(3):
                    for _r, _s in [(-1,0), (1,0), (0,-1), (0,1)]:
                        _t = _p + _r
                        _u = _q + _s
                        if 0 <= _t < 3 and 0 <= _u < 3:
                            if abs(image[a + _p][b + _q] - image[a + _t][b + _u]) > threshold:
                                return False
            return True

        def _avg_sum(c: int, d: int) -> int:
            _v = 0
            for _w in range(3):
                for _x in range(3):
                    _v += image[c + _w][d + _x]
            _y = _v // 9  # average as integer division
            return _y

        _z = len(image)
        __a = len(image[0])
        __b = [[0]*__a for _ in range(_z)]
        __c = [[0]*__a for _ in range(_z)]

        for __k in range(_z - 2):
            for __l in range(__a - 2):
                if _check_region(__k, __l):
                    __m = _avg_sum(__k, __l)
                    for __n in range(3):
                        for __o in range(3):
                            __b[__k + __n][__l + __o] += __m
                            __c[__k + __n][__l + __o] += 1

        for __p in range(_z):
            for __q in range(__a):
                if __c[__p][__q] > 0:
                    __b[__p][__q] = __b[__p][__q] // __c[__p][__q]
                else:
                    __b[__p][__q] = image[__p][__q]

        return __b