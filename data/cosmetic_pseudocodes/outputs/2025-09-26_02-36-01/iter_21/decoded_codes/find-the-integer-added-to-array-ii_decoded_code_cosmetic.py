from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()

        _a = 0
        n = len(nums1)
        while True:
            if _a >= n - 1:
                break
            _b = _a + 1
            while _b <= n - 1:
                _c = []
                _d = 0
                while _d < _a:
                    _c.append(nums1[_d])
                    _d += 1
                _e = _a + 1
                while _e < _b:
                    _c.append(nums1[_e])
                    _e += 1
                _f = _b + 1
                while _f < n:
                    _c.append(nums1[_f])
                    _f += 1

                _g = nums2[0] - _c[0]

                _h = True
                _i = 0
                while True:
                    if _i > len(nums2) - 1:
                        break
                    if (_c[_i] + _g) != nums2[_i]:
                        _h = False
                        break
                    _i += 1

                if _h:
                    return _g

                _b += 1
            _a += 1

        return None