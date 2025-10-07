class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        def intersecting_square_area(bl1, tr1, bl2, tr2):
            _xMaxLeft = bl1[0] if bl1[0] > bl2[0] else bl2[0]
            _xMinRight = tr1[0] if tr1[0] < tr2[0] else tr2[0]
            _yMaxBottom = bl1[1] if bl1[1] > bl2[1] else bl2[1]
            _yMinTop = tr1[1] if tr1[1] < tr2[1] else tr2[1]

            if not (_xMaxLeft < _xMinRight and _yMaxBottom < _yMinTop):
                return 0

            _sqSide = (_xMinRight - _xMaxLeft) if (_xMinRight - _xMaxLeft) < (_yMinTop - _yMaxBottom) else (_yMinTop - _yMaxBottom)
            return _sqSide * _sqSide

        _maxAreaFound = 0
        _lengthBottomLeft = len(bottomLeft)

        _outerIndex = 0
        while _outerIndex < (_lengthBottomLeft - 1):
            _innerIndex = _outerIndex + 1
            while _innerIndex < _lengthBottomLeft:
                _currentArea = intersecting_square_area(
                    bottomLeft[_outerIndex], topRight[_outerIndex],
                    bottomLeft[_innerIndex], topRight[_innerIndex]
                )
                if _maxAreaFound < _currentArea:
                    _maxAreaFound = _currentArea
                _innerIndex += 1
            _outerIndex += 1

        return _maxAreaFound