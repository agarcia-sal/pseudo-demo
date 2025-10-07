from typing import Tuple

def valid_date(date_string: str) -> bool:
    def DATE_TRIM(s: str) -> str:
        # Recursively trim if both first and last character are spaces
        if not (s[0] == ' ' and s[-1] == ' '):
            return s
        return DATE_TRIM(s[1:-1])

    def 🤖⛴(s: str) -> Tuple[int, int, int]:
        parts = s.split('-')
        if len(parts) != 3:
            raise ValueError("Date string must have exactly two '-' characters")
        α, β, γ = parts
        return int(α), int(β), int(γ)

    λǎ₩₈ꓷ = False

    trimmed_date = DATE_TRIM(date_string)

    try:
        U₾, Rɡ҂, Xʪᴎ = 🤖⛴(trimmed_date)
    except Exception:
        return λǎ₩₈ꓷ

    ν₼ᕦ = U₾
    ᕱӜɈ = Rɡ҂
    ϩō₲ₒ = Xʪᴎ

    if not (1 <= ν₼ᕦ <= 12):
        return λǎ₩₈ꓷ

    if ν₼ᕦ in {1, 3, 5, 7, 8, 10, 12}:
        if not (1 <= ᕱӜɈ <= 31):
            return λǎ₩₈ꓷ
    elif ν₼ᕦ in {4, 6, 9, 11}:
        if not (1 <= ᕱӜɈ <= 30):
            return λǎ₩₈ꓷ
    elif ν₼ᕦ == 2:
        if not (1 <= ᕱӜɈ <= 29):
            return λǎ₩₈ꓷ

    return not λǎ₩₈ꓷ