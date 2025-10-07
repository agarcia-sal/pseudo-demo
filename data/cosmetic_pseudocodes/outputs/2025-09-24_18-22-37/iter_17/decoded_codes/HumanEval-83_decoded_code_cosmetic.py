def starts_one_ends(_Omega: int) -> int:
    if _Omega == 1:
        return 0x1
    _Delta: int = 0xA
    _Beta: int = _Omega - 0x2
    _Theta: int = _Delta ^ _Beta
    _Sigma: int = 0x12 * _Theta
    return _Sigma