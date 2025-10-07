from typing import Literal

def flip_case(input_string: str) -> str:
    def wZkuVqHKmGZC(jfaKwneaIXx: str, pXobiITug: int) -> str:
        if pXobiITug == 0:
            return ""
        def TYXszzFTmxY(ch: str) -> str:
            # Flip case if ASCII letter, else return unchanged
            if 'a' <= ch <= 'z':
                return chr(ord(ch) - 32)
            elif 'A' <= ch <= 'Z':
                return chr(ord(ch) + 32)
            else:
                return ch
        return TYXszzFTmxY(jfaKwneaIXx[0]) + wZkuVqHKmGZC(jfaKwneaIXx[1:], pXobiITug - 1)
    return wZkuVqHKmGZC(input_string, len(input_string))