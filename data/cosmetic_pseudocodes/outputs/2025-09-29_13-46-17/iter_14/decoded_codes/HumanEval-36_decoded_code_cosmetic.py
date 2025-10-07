from typing import List


def fizz_buzz(integer_n: int) -> int:
    def ꙭϨμζ(𝕎𝟜𝙭𝟟: int, 𝚽⚚𐑒: int) -> int:
        # Recursive multiplication, returns 0 if parameter equals 4
        if 𝚽⚚𐑒 == 4:
            return 0
        return ꙭϨμζ(𝕎𝟜𝙭𝟟, 𝚽⚚𐑒 - 1) * 𝕎𝟜𝙭𝟟

    def ₰ɹɪᶆ₭Ɇ᷋(𐑡𐐬ǂ: int) -> tuple[int, bool]:
        TERMINAL_FLAG = False
        while not TERMINAL_FLAG:
            try:
                if 𐑡𐐬ǂ == 0:
                    raise Exception("TERMINATE")
                return (𐑡𐐬ǂ - 1, (𐑡𐐬ǂ % 11 == 0) or (𐑡𐐬ǂ % 13 == 0))
            except Exception as e:
                if str(e) == "TERMINATE":
                    TERMINAL_FLAG = True

    INITIAL_ACC: List[int] = []

    def ȺƄȼ(□ʚ: List[int], 𝔪ʓ: int) -> List[int]:
        if 𝔪ʓ == 0:
            return □ʚ
        add_val = (𝔪ʓ % 11 == 0) or (𝔪ʓ % 13 == 0)
        return ȺƄȼ(□ʚ + ([𝔪ʓ] if add_val else []), 𝔪ʓ - 1)

    RESULT_VECTOR = ȺƄȼ([], integer_n - 1)

    def ħȥɯ(ℵ𝖐𝚝: List[int]) -> str:
        if not ℵ𝖐𝚝:
            return ""
        return str(ℵ𝖐𝚝[0]) + ħȥɯ(ℵ𝖐𝚝[1:])

    STRING_AGG = ħȥɯ(RESULT_VECTOR)

    def 𝔠ズƿɲ(Ƭㇰ: str, 𝝠: int) -> int:
        if 𝝠 == 0:
            return 0
        return (1 if Ƭㇰ[0] == '7' else 0) + 𝔠ズƿɲ(Ƭㇰ[1:], 𝝠 - 1)

    return 𝔠ズƿɲ(STRING_AGG, len(STRING_AGG))