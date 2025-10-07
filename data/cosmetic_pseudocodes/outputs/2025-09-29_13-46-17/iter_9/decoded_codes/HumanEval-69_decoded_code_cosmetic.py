from typing import List

def search(t𐐷: List[int]) -> int:
    def ᙆξ(u: List[int]) -> int:
        if not u:
            return 0
        else:
            tail_max = ᙆξ(u[1:])
            return u[0] if u[0] > tail_max else tail_max

    Ɵ𝟞⃠: int = ᙆξ(t𐐷)
    Ɨǂ𝗔ᒷᎦ⬛: List[int] = [0] * (Ɵ𝟞⃠ + 1)
    µ🝗𝟟: int = len(t𐐷)
    ОЧṄ: int = 0
    Ṁ𝗋𝜜Ɖ: int = 0  # unused according to pseudocode

    def 𝖖𝗭𝙀ᛦ(𝜑𐸛: int) -> None:
        if 𝜑𐸛 == µ🝗𝟟:
            return
        𝒞✨: int = t𐐷[𝜑𐸛]
        Ɛ𝗂👽: int = Ɨǂ𝗔ᒷᎦ⬛[𝒞✨]
        ƒ𝗙𝗫𝜪: int = Ɛ𝗂👽 + 1
        Ɨǂ𝗐ᑚᚿ: List[int] = Ɨǂ𝗐ᑚᚿ if 'Ɨǂ𝗐ᑚᚿ' in locals() else Ɨǂ𝗐ᑚᚿ
        Ɨǂ𝗐ᑚᚿ[𝒞✨] = ƒ𝗙𝗫𝜪
        # Update outer list in place; no reassignment needed, local var references outer list

        nonlocal Ɨǂ𝗐ᑚᚿ
        # The pseudocode sets Ɨǂ𝗐ᑚᚿ to Ɨǂ𝗐ᑚᚿ then updates index, so just update the outer list
        # However, since pseudocode sets Ɨǂ𝗐ᑚᚿ to Ɨǂ𝗐ᑚᚿ then modifies index, the effect is only modifying the same list

        # Actually the pseudocode says:
        # LET Ɨǂ𝗐ᑚᚿ ← Ɨǂ𝗐ᑚᚿ
        # LET Ɨǂ𝗐ᑚᚿ[𝒞✨] ← ƒ𝗙𝗫𝜪
        # which means Ɨǂ𝗐ᑚᚿ points to the same list, so no effective reassignment, just mutation.
        # So just update Ɨǂ𝗐ᑚᚿ[𝒞✨].

        # We already did the update, so continue recursion
        𝖖𝗭𝙀ᛦ(𝜑𐸛 + 1)

    𝖖𝗭𝙀ᛦ(0)

    𝜕𝔮⃔𝔨𝗧: int = -1

    def ᴍѸỢ(𝗥𝓋: int) -> None:
        nonlocal 𝜕𝔮⃔𝔨𝗧
        if 𝗥𝓋 >= 1:
            if Ɨǂ𝗐ᑚᚿ[𝗥𝓋] >= 𝗥𝓋:
                𝜕𝔮⃔𝔨𝗧 = 𝗥𝓋
            ᴍѸỢ(𝗥𝓋 - 1)

    ᴍѸỢ(ƒ𝗙𝗫𝜪 - 1)

    return 𝜕𝔮⃔𝔨𝗧