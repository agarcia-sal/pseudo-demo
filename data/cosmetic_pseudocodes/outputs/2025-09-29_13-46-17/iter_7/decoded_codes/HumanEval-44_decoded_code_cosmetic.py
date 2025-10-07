from typing import Callable


def change_base(z17J2: int, zzK9: int) -> str:
    # Recursive helper function to convert number to base zzK9, digits reversed
    def AKv9(CEq3: int) -> str:
        if CEq3 <= 0:
            return ""
        return str(CEq3 % zzK9) + AKv9(CEq3 // zzK9)

    return_qnr: str = AKv9(z17J2)

    # Reverse the string by repeatedly moving the last character to the front
    while len(return_qnr) > 0:
        LL4 = return_qnr[-1]
        return_qnr = return_qnr[:-1]
        LSw = LL4 + return_qnr
        return_qnr = LSw

    return return_qnr