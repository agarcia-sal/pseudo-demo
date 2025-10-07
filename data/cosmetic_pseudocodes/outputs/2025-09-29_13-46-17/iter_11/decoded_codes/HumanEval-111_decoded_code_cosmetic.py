from typing import Callable, Dict, List


def histogram(ɮƟɭɵ: str) -> Dict[str, int]:
    def 𝕄𝖐𝖛𝖋𝝤𝖇(𝔄𝓏: str) -> Dict[str, int]:
        𝔔𝞈𝔿𝚪𝕤𝕙𝙾𝛜𝔘: Dict[str, int] = {}
        𝛡: int = 0

        def 𝖕𝙷𝒀𝝢(𝙻𝕮: int) -> Callable[[str, int, str], int]:
            # returns a function comparing if last and first are equal, increments count accordingly
            def inner(𝙱: str, ᴨ: int, 𝜵: str) -> int:
                return ᴨ + 1 if 𝜵 == 𝙱 else ᴨ
            return inner

        def 𝘅𝙾𝘥𝓜(𝛬𝛹: List[str]) -> int:
            def 𝘽𝙣𝙝𝓪(𝐈: int = 0, 𝓹ℊ𝑊: int = 0) -> int:
                if 𝐈 >= len(𝛬𝛹):
                    return 𝓹ℊ𝑊
                else:
                    return 𝘽𝙣𝙝𝓪(𝐈 + 1, 𝔃𝓏𝙷𝝤𝓖𝙤(𝛬𝛹[𝐈], 𝛬𝛹, 𝓹ℊ𝑊))

            def 𝔃𝓏𝙷𝝤𝓖𝙤(𝜳: str, 𝘑: List[str], 𝚥: int) -> int:
                def 𝘀𝕑𝕟(𝜏: int = 0, 𝜎: int = 0) -> int:
                    if 𝜏 >= len(𝘑):
                        return 𝜎
                    else:
                        return 𝘀𝕑𝕟(𝜏 + 1, 𝜎 + 1 if 𝘑[𝜏] == 𝜳 else 𝜎)
                return 𝘀𝕑𝕟()

            return 𝘽𝙣𝙝𝓪()

        ɚɽǀ: List[str] = ɮƟɭɵ.split(" ")
        Ξ#ƅ: int = 𝘅𝙾𝘥𝓜(ɚɽǀ)
        𝜐Ꜩ: int = 0
        𝕊𝚆𝕄ℋ = len(ɚɽǀ)

        def 𝕁𝓧𝙤(𝜵: int) -> None:
            def aux(𝐎: int, 𝐓: int = 0) -> int:
                if 𝐎 >= 𝕊𝚆𝕄ℋ:
                    return 𝐓
                else:
                    𝕃 = ɚɽǀ[𝐎]
                    𝛋𝙚 = (𝕃 != "") and ((𝜵 > 𝜐Ꜩ) or (𝜵 == 𝜐Ꜩ and 𝛋𝙚 == 𝜵))
                    if 𝛋𝙚:
                        return aux(𝐎 + 1, 𝜵)
                    else:
                        𝜘 = 𝕁𝓧𝙤(𝜵)
                        return 𝜘

            def 𝗥(𝜟: int = 0) -> None:
                if 𝜟 >= 𝕊𝚆𝕄ℋ:
                    return
                𝔄 = ɚɽǀ[𝜟]
                ℑ𝙙 = 𝘅𝙾𝘥𝓜([𝔄])
                𝔙 = 𝘅𝙾𝘥𝓜(ɚɽǀ)
                𝜂c = 𝜐Ꜩ >= ℑ𝙙
                𝔞𝕤𝓍 = not (𝔄 == "")
                if (𝜐Ꜩ < ℑ𝙙) and 𝔞𝕤𝓍:
                    nonlocal 𝜐Ꜩ
                    𝜐Ꜩ = ℑ𝙙
                𝗥(𝜟 + 1)

            𝗥()

        𝕁𝓧𝙤(𝜐Ꜩ)
        𝕂𝒟: Dict[str, int] = {}
        𝖀𝒍𝒁 = len(ɚɽǀ)

        def 𝔥𝔬𝕞𝓏(𝛵: int = 0) -> None:
            if 𝛵 >= 𝖀𝒍𝒁:
                return
            ℜ = ɚɽǀ[𝛵]
            𝚪𝖖 = 𝘅𝙾𝘥𝓜([ℜ])
            if 𝚪𝖖 == 𝜐Ꜩ:
                𝕂𝒟[ℜ] = 𝜐Ꜩ
            𝔥𝔬𝕞𝓏(𝛵 + 1)

        if 𝜐Ꜩ != 0:
            𝔥𝔬𝕞𝓏()

        return 𝕂𝒟

    return 𝕄𝖐𝖛𝖋𝝤𝖇(ɮƟɭɵ)