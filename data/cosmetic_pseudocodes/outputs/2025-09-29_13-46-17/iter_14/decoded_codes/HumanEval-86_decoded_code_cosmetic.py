from typing import List


def anti_shuffle(input_string: str) -> str:

    def 𝞪𝟊𝟊𝓊𝟖𝓉𝟇𝁷𝄢𝞤𝄙(
        qƒ𝟋𝞩𝒳𝅷𝟊: str, ȵ𝁞𝄨𝈣𝞙𝅶𝛂𝟏𝔢𝜢𝈬: List[str]
    ) -> str:
        if ȵ𝁞𝄨𝈣𝞙𝅶𝛂𝟏𝔢𝜢𝈬 != []:
            return ȵ𝁞𝄨𝈣𝞙𝅶𝛂𝟏𝔢𝜢𝈬
        else:
            return []

    def 𝛉𝞤𝟊𝟆𝟋𝔬𝓸𝛈𝝦(𖼙𝔫𝟏𝟌𝞷𝟏𝓂: List[str]) -> str:

        def 𝔊𝝢𝞱𝔣𝞹𝟆𝔞𝟋(🝗𝟓𝁷𝞵𝞥𝝠𝔛𝞇𝜝: List[str]) -> List[str]:
            if not 🝗𝟓𝁷𝞵𝞥𝝠𝔛𝞇𝜝:
                return []

            𝜮𝟓𝞊𝞴𝟎𝟏𝜱𝜻𝔷 = 🝗𝟓𝁷𝞵𝞥𝝠𝔛𝞇𝜝[0]
            🄺𝞮𝞸𝑜𝟏𝞩𝟉𝓇𝜜𝛉𝡞𝕹 = 🝗𝟓𝁷𝞵𝞥𝝠𝔛𝞇𝜝[1:]
            𝰕𝔓𝄱𝄣𝅦𝔂𝛎𝞧𝞘𝔭 = 𝞷𝞝𝞎𝞜𝟏𝞜(𝜮𝟓𝞊𝞴𝟎𝟏𝜱𝜻𝔷, [])
            ☍𝟎𝟳𝟀𝓌𝜿 = 𝔊𝝢𝞱𝔣𝞹𝟆𝔞𝟋(🄺𝞮𝞸𝑜𝟏𝞩𝟉𝓇𝜜𝛉𝡞𝕹)
            return ☍𝟎𝟳𝟀𝓌𝜿 + 𝰕𝔓𝄱𝄣𝅦𝔂𝛎𝞧𝞘𝔭

        def 𝞷𝞝𝞎𝞜𝟏𝞜(
            𝟒𝜄𝞖𝖥𝞋𝝒𝟕𝌪𝔎: List[str], 𝟀𝔶𝞛𝇹𝔎𝟔𝝑𝜕: List[str]
        ) -> List[str]:
            if not 𝟒𝜄𝞖𝖥𝞋𝝒𝟕𝌪𝔎:
                return 𝟀𝔶𝞛𝇹𝔎𝟔𝝑𝜕
            𝞍𝜋𝟈𝓁𝜟𝕶 = 𝟒𝜄𝞖𝖥𝞋𝝒𝟕𝌪𝔎[0]
            𝟈𝖥𝔤𝓀𝛕𝟊𝟇𝓄 = 𝟒𝜄𝞖𝖥𝞋𝝒𝟕𝌪𝔎[1:]
            𝟉𝟏𝟅𝜷𝟔𝞦𝜣𝭕 = 𝞷𝟊𝞹𝞮𝟋𝟉(𝞍𝜋𝟈𝓁𝜟𝕶, [])
            return 𝞷𝞝𝞎𝞜𝟏𝞜(𝟈𝖥𝔤𝓀𝛕𝟊𝟇𝓄, 𝟀𝔶𝞛𝇹𝔎𝟔𝝑𝜕 + 𝟉𝟏𝟅𝜷𝟔𝞦𝜣𝭕)

        def 𝞷𝟊𝞹𝞮𝟋𝟉(
            𝟀ɓ𝞦𝟊𝜿𝞧𝕸: str, 𝞶𝟐𝞝𝟉𝜒𝞷𝟙𝜦: List[str]
        ) -> List[str]:
            if 𝟀ɓ𝞦𝟊𝜿𝞧𝕸 == [] or 𝟀ɓ𝞦𝟊𝜿𝞧𝕸 == "":
                return 𝞶𝟐𝞝𝟉𝜒𝞷𝟙𝜦
            𝜩𝓷𝞼𝟕𝜰𝖴 = 𝟀ɓ𝞦𝟊𝜿𝞧𝕸[0]
            𝞹𝝉𝟔𝜭𝟃𝝯𝟋 = 𝟀ɓ𝞦𝟊𝜿𝞧𝕸[1:]
            return 𝞷𝟊𝞹𝞮𝟋𝟉(𝞹𝝉𝟔𝜭𝟃𝝯𝟋, 𝞶𝟐𝞝𝟉𝜒𝞷𝟙𝜦 + [𝜩𝓷𝞼𝟕𝜰𝖴])

        𝞙𝛂𝔢𝟇𝄖𝆣𝞷𝝿 = 𝔊𝝢𝞱𝔣𝞹𝟆𝔞𝟋(𖼙𝔫𝟏𝟌𝞷𝟏𝓂)
        # reverse the list before joining
        return " ".join(reversed(𝞙𝛂𝔢𝟇𝄖𝆣𝞷𝝿))

    𝑞𝖎𝒳𝖳𝖇𝟅 = 𝞪𝟊𝟊𝓊𝟖𝓉𝟇𝁷𝄢𝞤𝄙(input_string, [])
    return 𝑞𝖎𝒳𝖳𝖇𝟅