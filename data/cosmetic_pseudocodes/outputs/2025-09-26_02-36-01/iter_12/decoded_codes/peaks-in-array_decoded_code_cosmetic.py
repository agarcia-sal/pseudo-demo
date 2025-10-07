class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def _checkPeak(position: int) -> bool:
            return nums[position] > nums[position - 1] and nums[position] > nums[position + 1]

        def LeftInsertPosition(arr: list[int], val: int) -> int:
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] < val:
                    l = m + 1
                else:
                    r = m
            return l

        def RightInsertPosition(arr: list[int], val: int) -> int:
            l, r = 0, len(arr)
            while l < r:
                m = (l + r) // 2
                if arr[m] <= val:
                    l = m + 1
                else:
                    r = m
            return l

        def Contains(arr: list[int], val: int) -> bool:
            # Since arr is sorted, we can use binary search instead of linear search for efficiency
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == val:
                    return True
                elif arr[m] < val:
                    l = m + 1
                else:
                    r = m - 1
            return False

        def InsertSorted(arr: list[int], val: int) -> list[int]:
            pos = LeftInsertPosition(arr, val)
            return arr[:pos] + [val] + arr[pos:]

        def RemoveValue(arr: list[int], val: int) -> list[int]:
            # Since arr is sorted, we can find position by binary search to remove efficiently
            pos = LeftInsertPosition(arr, val)
            if pos < len(arr) and arr[pos] == val:
                return arr[:pos] + arr[pos + 1 :]
            return arr

        def Max(a: int, b: int) -> int:
            return a if a > b else b

        def Min(a: int, b: int) -> int:
            return a if a < b else b

        _accumulator = []
        n = len(nums)
        for _idx in range(1, n - 1):
            if _checkPeak(_idx):
                _accumulator.append(_idx)

        _output = []
        _queryPointer = 0
        qlen = len(queries)
        while _queryPointer < qlen:
            _currentQuery = queries[_queryPointer]

            if _currentQuery[0] == 1:
                _leftBoundary = _currentQuery[1]
                _rightBoundary = _currentQuery[2]

                _leftInsertPos = LeftInsertPosition(_accumulator, _leftBoundary + 1)
                _rightInsertPos = RightInsertPosition(_accumulator, _rightBoundary) - 1

                _output.append(_rightInsertPos - _leftInsertPos)
            else:
                _idxUpdate = _currentQuery[1]
                _valUpdate = _currentQuery[2]

                if nums[_idxUpdate] == _valUpdate:
                    _queryPointer += 1
                    continue

                nums[_idxUpdate] = _valUpdate

                _i = Max(1, _idxUpdate - 1)
                limit = Min(n - 2, _idxUpdate + 1)

                while True:
                    if _i > limit:
                        break

                    if _checkPeak(_i):
                        if not Contains(_accumulator, _i):
                            _accumulator = InsertSorted(_accumulator, _i)
                    else:
                        if Contains(_accumulator, _i):
                            _accumulator = RemoveValue(_accumulator, _i)
                    _i += 1

            _queryPointer += 1

        return _output