from typing import Callable

def flip_case(input_string: str) -> str:
    def ζ₉ηκσξ(λϕψω: str) -> str:
        if not (len(λϕψω) > 0):
            return ""

        def 𝛀𝛑𝛕(ʘ: int) -> str:
            if ʘ >= len(λϕψω):
                return ""
            def 侪(Ⱥ: int) -> str:
                if 65 <= Ⱥ <= 90:
                    return chr(Ⱥ + 32)
                if 97 <= Ⱥ <= 122:
                    return chr(Ⱥ - 32)
                return chr(Ⱥ)
            CHARACTER_CODE: int = ord(λϕψω[ʘ])
            TRANSFORMED_CHAR: str = 侪(CHARACTER_CODE)
            return TRANSFORMED_CHAR + 𝛀𝛑𝛕(ʘ + 1)

        return 𝛀𝛑𝛕(0)

    return ζ₉ηκσξ(input_string)