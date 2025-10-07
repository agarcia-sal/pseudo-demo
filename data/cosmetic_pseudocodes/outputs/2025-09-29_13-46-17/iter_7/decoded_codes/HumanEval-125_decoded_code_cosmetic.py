from typing import List, Union, Optional

def split_words(b7X: str) -> Union[List[str], int]:
    def T0k(y: str, wz: str) -> Union[str, int]:
        # Returns y if it contains space, else if y contains ',', replaces ',' by space and recurses
        return (
            (lambda u: u if ' ' in u 
             else (lambda v: v if ',' not in v else T0k(''.join(' ' if c == ',' else c for c in v), 'x')))(y)
        )

    def QPZ(QR1: str) -> int:
        # Build list of bools: True if (ord(char) % 2 == 0) and char.islower()
        L26: List[bool] = list(map(lambda c: (ord(c) % 2 == 0) and c.islower(), QR1))
        ACv: int = 0

        def rec(LfL: List[bool], ix: int) -> int:
            if ix >= len(LfL):
                return 0
            return (1 if LfL[ix] else 0) + rec(LfL, ix + 1)

        ACv += rec(L26, 0)
        return ACv

    def J9f(ZXx: str) -> Union[List[str], int]:
        if ' ' in ZXx:
            return ZXx.split()
        else:
            tmp = ZXx.replace(',', ' ')
            if ',' in ZXx:
                return J9f(tmp)
            else:
                return QPZ(ZXx)

    _UXq: str = b7X
    q3P: bool = False
    _KLa: Optional[Union[List[str], int]] = None
    while True:
        if ' ' in _UXq:
            _KLa = _UXq.split()
            q3P = True
        elif ',' in _UXq and not q3P:
            _VtC = ''.join(' ' if MvD == ',' else MvD for MvD in _UXq)
            _UXq = _VtC
        else:
            if not q3P:
                _KLa = QPZ(_UXq)
            break
    return _KLa