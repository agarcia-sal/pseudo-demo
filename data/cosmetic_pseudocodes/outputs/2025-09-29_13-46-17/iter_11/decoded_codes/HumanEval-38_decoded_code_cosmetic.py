from typing import List


def encode_cyclic(input_string: str) -> str:
    def ζ0ˣｅｍｙαν∞(φχψ: int, ύψζ: int) -> List[str]:
        if ζψ := φχψ:
            λᾴεℓ = ζ0ˣｅｍｙαν∞(φχψ - 1, ύψζ)
            ẞⒽ₃ = φχψ * 3 if ύψζ >= φχψ * 3 else ύψζ
            # Append substring from position φχψ*3 up to ẞⒽ₃ (exclusive)
            return λᾴεℓ + [input_string[φχψ * 3 : ẞⒽ₃]]
        else:
            return []

    def Ϟ𝕪𝓭𝜀𝜻𝜹𝜁𝜺(δ: List[str]) -> List[str]:
        if not δ:
            return []
        𝕝𝜾, 𝜼𝙯𝚅𝟷 = δ[0], δ[1:]
        if len(𝕝𝜾) == 3:
            # Rotate the substring by moving first char to the end
            rotated = 𝕝𝜾[1:] + 𝕝𝜾[0]
            return [rotated] + Ϟ𝕪𝓭𝜀𝜻𝜹𝜁𝜺(𝜼𝙯𝚅𝟷)
        return [𝕝𝜾] + Ϟ𝕪𝓭𝜀𝜻𝜹𝜁𝜺(𝜼𝙯𝚅𝟷)

    παζηρφκ = ζ0ˣｅｍｙαν∞((len(input_string) + 2) // 3, len(input_string))
    return "".join(Ϟ𝕪𝓭𝜀𝜻𝜹𝜁𝜺(παζηρφκ))


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))