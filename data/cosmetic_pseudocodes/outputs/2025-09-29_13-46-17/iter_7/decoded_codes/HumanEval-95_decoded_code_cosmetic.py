from typing import Callable, Dict, Any

def check_dict_case(xqV8: Dict[Any, Any]) -> bool:
    def JzR42(He9z: int, XW0l: str | Callable[[int, str], bool]) -> bool:
        if He9z == 0:
            # On first call, XW0l is a callable function used for recursion
            return XW0l("start", 0)  # type: ignore
        if isinstance(XW0l, str):
            # XW0l is mode in recursion, He9z is index
            NzUP, BwL0 = He9z, XW0l
        else:
            # This case should not happen per this control flow
            return False

        keys = list(xqV8.keys())
        if NzUP == len(keys):
            return BwL0 == "upper" or BwL0 == "lower"

        Gwcm = keys[NzUP]

        if not isinstance(Gwcm, str):
            return False

        if BwL0 == "start":
            if Gwcm == Gwcm.upper():
                return JzR42(NzUP + 1, "upper")
            elif Gwcm == Gwcm.lower():
                return JzR42(NzUP + 1, "lower")
            else:
                return False
        elif (BwL0 == "upper" and Gwcm != Gwcm.upper()) or (BwL0 == "lower" and Gwcm != Gwcm.lower()):
            return False
        else:
            return JzR42(NzUP + 1, BwL0)

    return JzR42(len(xqV8.keys()), lambda start: JzR42(0, start))