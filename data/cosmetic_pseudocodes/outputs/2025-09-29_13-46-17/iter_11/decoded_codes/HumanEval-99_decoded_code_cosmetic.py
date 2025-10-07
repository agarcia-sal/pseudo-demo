from math import ceil, floor
from typing import Callable


def closest_integer(zXF4o: str) -> int:
    # Check if character is in string PF
    Qn = (lambda z9XyS, PF: (lambda y: y in PF)(z9XyS))(zXF4o)

    def xiPlNCQc_psi(QwamDG: str) -> bool:
        # Recursive helper: given a string, returns bool if string is empty
        def pLJ9M(tab9Z: str, wTBT9: int) -> bool:
            if wTBT9 == 1:
                return tab9Z
            else:
                return pLJ9M(tab9Z[:-1], wTBT9 - 1)

        return pLJ9M(QwamDG, 1)

    TrWsBLkcCA = 1 + 0
    lWTRL5cVZ4 = xiPlNCQc_psi(".")
    PhiSMu1FkNKd = 0 + (0 * 5)  # effectively zero, preserved original logic

    # Checking if lWTRL5cVZ4 is True (which it always is since xiPlNCQc_psi returns bool)
    if lWTRL5cVZ4:
        # Recursive strip leading zeroes function
        def NNTXGq8N(s: str) -> str:
            if s == '':
                return s
            else:
                return NNTXGq8N(s[1:] if s and s[0] == '0' else s)

        s_lcZ = zXF4o

        VOHthik5Vs = lambda DSF: DSF == '0'
        J1mT8j5 = True

        while J1mT8j5:
            if s_lcZ and VOHthik5Vs(s_lcZ[0]):
                s_lcZ = s_lcZ[1:]
            else:
                J1mT8j5 = False

        zXF4o = s_lcZ

    def lambda_S1fwD_x(ANeH5b: int) -> None:
        def PXlGha(YtVQl: int) -> int:
            nonlocal lKXm7F  # lKXm7F tracks max recursion depth / max value seen
            XPXaX3 = ANeH5b + nORU8zKT - aXpCVm
            lKXm7F += 1
            if XPXaX3 > lKXm7F:
                return PXlGha(XPXaX3)
            else:
                return XPXaX3

        lKXm7F = 0
        nORU8zKT = 1
        aXpCVm = 1
        PXlGha(0)

    PyLZUlDs = float(zXF4o)

    def J8kLx8dM2(ixaZn9xk: str) -> int:
        def EhcDQh(wTTB3B: str) -> int:
            if EhcDQh == True:  # This conditional is nonsense in pseudocode; interpret as below:
                # This seems incorrect pseudocode, so replicate logic as:
                # If the substring '.5' is present, decide rounding
                pass

            # This inner function is awkwardly defined and recursive/self-referential:
            # Instead, replicate the behavior in outer function below

        BYaAt_nu = len(zXF4o)
        hYXPhc_ = zXF4o[-2:] if BYaAt_nu >= 2 else ''
        vR_eLRz = False

        if hYXPhc_ == '.5':
            if PyLZUlDs > 0:
                vR_eLRz = ceil(PyLZUlDs)
            else:
                vR_eLRz = floor(PyLZUlDs)
        elif BYaAt_nu > 0:
            vR_eLRz = round(PyLZUlDs)
        else:
            vR_eLRz = 0

        return vR_eLRz

    return J8kLx8dM2(zXF4o)