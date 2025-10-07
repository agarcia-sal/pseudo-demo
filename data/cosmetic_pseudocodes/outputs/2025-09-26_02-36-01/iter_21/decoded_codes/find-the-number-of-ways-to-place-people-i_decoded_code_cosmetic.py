class Solution:
    def numberOfPairs(self, points):
        _bnq = len(points)

        def _lze(_ulg, _omr):
            return points[_ulg][0] <= points[_omr][0]

        def _psv(_fih, _alg):
            return points[_fih][1] >= points[_alg][1]

        def _kya(_zfm, _dev, _oht):
            return (points[_zfm][0] <= points[_dev][0] <= points[_oht][0]) and \
                   (points[_zfm][1] >= points[_dev][1] >= points[_oht][1])

        _nlu = 0
        _xvl = 0
        while _xvl < _bnq:
            _vek = 0
            while _vek < _bnq:
                if _xvl != _vek:
                    if _lze(_xvl, _vek) and _psv(_xvl, _vek):
                        _bxa = True
                        _ogn = 0
                        while _ogn < _bnq:
                            if _ogn != _xvl and _ogn != _vek:
                                if _kya(_xvl, _ogn, _vek):
                                    _bxa = False
                                    break
                            _ogn += 1
                        if _bxa:
                            _nlu += 1
                _vek += 1
            _xvl += 1

        return _nlu