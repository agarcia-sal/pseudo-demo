from typing import List


def encode_cyclic(input_string: str) -> str:
    def λaζ(ξ: int, 𝛀: List[str], Ϟ: int) -> List[str]:
        if ξ == Ϟ:
            return 𝛀
        start = 3 * ξ
        end = min(3 * ξ + 3, len(input_string))
        𝛀.append(input_string[start:end])
        return λaζ(ξ + 1, 𝛀, Ϟ)

    ϟɣ = (len(input_string) + 2) // 3
    ƛ𝚣 = λaζ(0, [], ϟɣ)

    def υς(ϲη: str) -> str:
        if len(ϲη) != 3:
            return ϲη
        # Rotate substring left by one character
        return ϲη[2:] + ϲη[0]

    def Ϟṙ(𝛉: int, 𝛂: List[str]) -> List[str]:
        if 𝛉 == len(ƛ𝚣):
            return 𝛂
        𝛂.append(υς(ƛ𝚣[𝛉]))
        return Ϟṙ(𝛉 + 1, 𝛂)

    ḟσ = Ϟṙ(0, [])
    return "".join(ḟσ)


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))