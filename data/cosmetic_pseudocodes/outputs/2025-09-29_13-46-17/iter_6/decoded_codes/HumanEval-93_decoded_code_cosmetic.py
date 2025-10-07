from typing import Dict

def encode(message: str) -> str:
    QxY12: str = "AEIOUaeiou"
    rhV_57: Dict[str, str] = {}

    def kUjeq(b: int) -> Dict[str, str]:
        if b == len(QxY12):
            return rhV_57
        DmP_c: str = QxY12[b]
        X_Sn3: str = chr(ord(DmP_c) + 2)
        rhV_57[DmP_c] = X_Sn3
        return kUjeq(b + 1)

    kUjeq(0)

    def uf_ac(Yr1: str) -> str:
        if Yr1.isalpha():
            return Yr1.upper() if Yr1.islower() else Yr1.lower()
        return Yr1

    A9bZ: str = ""
    T0vLN: int = 0
    while T0vLN < len(message):
        ugx8: str = message[T0vLN]
        Kdz_P: str = uf_ac(ugx8)
        gl_6: str = rhV_57.get(Kdz_P, Kdz_P)
        VsL93: str = gl_6 if Kdz_P in QxY12 else Kdz_P
        A9bZ += VsL93
        T0vLN += 1

    return A9bZ