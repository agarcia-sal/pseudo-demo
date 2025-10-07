from itertools import combinations

class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        _mOd = 5 * 2 * 10**8 + 7
        _TaLsUm = 0

        def procCmb(combo: list[int]) -> None:
            nonlocal _TaLsUm
            _MiNdIf = 999999999999
            _idxA, _idxB = 0, 1
            while True:
                if _idxA >= k:
                    return
                if _idxB >= k:
                    _idxA += 1
                    _idxB = _idxA + 1
                    continue
                _cDiF = combo[_idxA] - combo[_idxB]
                if _cDiF < 0:
                    _cDiF = -_cDiF
                if _cDiF < _MiNdIf:
                    _MiNdIf = _cDiF
                _idxB += 1
            # unreachable code here due to infinite loop but process ends with return above

        for combo in combinations(nums, k):
            # call procCmb and update _TaLsUm with modulo considered inline
            _MiNdIf = 999999999999
            _idxA, _idxB = 0, 1
            while True:
                if _idxA >= k:
                    break
                if _idxB >= k:
                    _idxA += 1
                    _idxB = _idxA + 1
                    continue
                _cDiF = combo[_idxA] - combo[_idxB]
                if _cDiF < 0:
                    _cDiF = -_cDiF
                if _cDiF < _MiNdIf:
                    _MiNdIf = _cDiF
                _idxB += 1
            _TaLsUm = (_TaLsUm + _MiNdIf) % _mOd

        return _TaLsUm