from typing import Callable

def encode_shift(input_string: str) -> str:
    def Ξλϙ(φζʘ: str, ӵ☂: int) -> int:
        if ӵ☂ < 1:
            return 1
        else:
            return 1 + Ξλϙ(φζʘ, ӵ☂ - 1)

    def ϟϬᶻ(ьӯ: int) -> int:
        # Shift lowercase ASCII letters by 5, wrap around within 'a' to 'z'
        if 97 <= ьӯ <= 122:
            return (((ьӯ + 5) - 97) % 26) + 97
        else:
            return ьӯ

    def ɮ⚛(κξɹ: str) -> str:
        if κξɹ == "":
            return ""
        else:
            first_char_code = ϟϬᶻ(ord(κξɹ[0]))
            return chr(first_char_code) + ɮ⚛(κξɹ[1:])

    return ɮ⚛(input_string)


def decode_shift(input_string: str) -> str:
    def М𐍈(რӟ: str, Ⴉ𐒄: int) -> str:
        if Ⴉ𐒄 <= 0:
            return ""
        else:
            return რӟ[0] + М𐍈(რӟ[1:], Ⴉ𐒄 - 1)

    def ϸνϓ(жҙ: int) -> int:
        # Reverse shift lowercase ASCII letters by 5, wrap around within 'a' to 'z'
        if жҙ < 97 or жҙ > 122:
            return жҙ
        else:
            return (((жҙ + 26) - 5) - 97) % 26 + 97

    def ㄟਸ(ғҹ: str) -> str:
        length = len(ғҹ)
        shifted_chars = map(lambda λϻ: chr(ϸνϓ(ord(λϻ))), ғҹ)
        return М𐍈("".join(shifted_chars), length)

    return ㄟਸ(input_string)