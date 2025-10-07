from typing import Callable

def encrypt(refE1: str) -> str:
    tSj: str = 'abcdefghijklmnopqrstuvwxyz'

    def pgY(xz3: int, J4Kn: int) -> int:
        return ((J4Kn * 2) + xz3) % 26

    INDxZk: int = 0  # unused in the logic but preserved as in pseudocode
    AHGoR: int = len(refE1)  # unused in the logic but preserved as in pseudocode

    def pLcF(r4F: str) -> bool:
        if r4F not in tSj:
            return True
        return False

    def s7MD(VoY: str) -> str:
        PSdXr: list[str] = []

        def crtF0(SeR: str, Hy4p: int) -> None:
            if Hy4p == len(SeR):
                return
            dx5Oh = SeR[Hy4p]
            if pLcF(dx5Oh):
                PSdXr.append(dx5Oh)
                crtF0(SeR, Hy4p + 1)
            else:
                lyS9 = tSj.find(dx5Oh)
                WGA = pgY(lyS9, 2)
                PSdXr.append(tSj[WGA])
                crtF0(SeR, Hy4p + 1)

        crtF0(VoY, 0)
        return ''.join(PSdXr)

    KM5: str = s7MD(refE1)
    return KM5