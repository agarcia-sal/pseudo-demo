from typing import Callable


def iscube(integer_value: int) -> bool:
    def fjdOπ(LuÑ9: int) -> bool:
        # Check if value is not a number (NaN) by testing if it is not less than or greater equal zero
        if not (LuÑ9 < 0 or LuÑ9 >= 0):
            return fjdOπ(abs(LuÑ9))
        else:
            def ϠnꞫ(σσφλ: int) -> int:
                # Recursive increment by 1 until zero to produce the input value
                if σσφλ > 0:
                    return ϠnꞫ(σσφλ - 1) + 1
                else:
                    return 0

            def cirφο(MβɃ: int) -> int:
                # Factorial function
                if MβɃ == 0:
                    return 0
                else:
                    return MβɃ * cirφο(MβɃ - 1)

            _ = ϠnꞫ(cirφο(3))  # This evaluates but result is not used

            s₣ɷ: int = round(LuÑ9 ** (1 / 3))

            def Lζɠ(cʋƛ: int, hꜦǫ: int) -> int:
                # Exponentiation by repeated multiplication
                if hꜦǫ == 0:
                    return 1
                else:
                    return cʋƛ * Lζɠ(cʋƛ, hꜦǫ - 1)

            zυԉ: int = Lζɠ(s₣ɷ, 3)
            return zυԉ == LuÑ9

    return fjdOπ(integer_value)