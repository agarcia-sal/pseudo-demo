from collections import Counter

class Solution:

    def maxPalindromesAfterOperations(self, words):
        _m = Counter(''.join(words))
        _q = 0
        _r = 0

        for _u in _m.values():
            _q += _u // 2
            _r += _u % 2

        self.SortAscendingByLength(words)

        _o = 0
        _x = 0

        while _x < len(words):
            _v = len(words[_x]) // 2

            if not (_q < _v):
                _q -= _v
                _o += 1

            _x += 1

        return _o

    def SortAscendingByLength(self, arr):
        _a = 0
        while _a < len(arr) - 1:
            _b = 0
            while _b < len(arr) - _a - 1:
                if len(arr[_b]) > len(arr[_b + 1]):
                    _c = arr[_b]
                    arr[_b] = arr[_b + 1]
                    arr[_b + 1] = _c
                _b += 1
            _a += 1