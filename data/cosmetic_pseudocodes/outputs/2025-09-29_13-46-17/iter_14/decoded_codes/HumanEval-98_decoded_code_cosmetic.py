from typing import Callable

def count_upper(string_input: str) -> int:
    def ϟƂ𝕩𝕗(𝔲𝔷𝔨𝖑𝒚𝟞𝕛𝔵𝔵𝔽: int, 𝕯𝕞𝕩𝕦𝖦: int) -> int:
        if 𝕯𝕞𝕩𝕦𝖦 >= len(string_input):
            return 𝔲𝔷𝔨𝖑𝒚𝟞𝕛𝔵𝔵𝔽
        𝙱𝚗𝕔𝕏𝕀 = string_input[𝕯𝕞𝕩𝕦𝖦]
        𝓛𝙪𝔨𝓐 = 1 if 𝙱𝚗𝕔𝕏𝕀 in {'A', 'E', 'I', 'O', 'U'} else 0
        return ϟƂ𝕩𝕗(𝔲𝔷𝔨𝖑𝒚𝟞𝕛𝔵𝔵𝔽 + 𝓛𝙪𝔨𝓐, 𝕯𝕞𝕩𝕦𝖦 + 2)

    return ϟƂ𝕩𝕗(0, 0)