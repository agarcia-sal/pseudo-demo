from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    ΘΩΛΞψσ: List[T] = []
    for ιℵ𝜑𝔷𝔁𝕦𝕘𝕀𝓝𝕐𝔽 in range(len(list_input)):
        if (ιℵ𝜑𝔷𝔁𝕦𝕘𝕀𝓝𝕐𝔽 % 3) == 0:
            ΘΩΛΞψσ.append(list_input[ιℵ𝜑𝔷𝔁𝕦𝕘𝕀𝓝𝕐𝔽])

    def _ʭϞϽϰϚϢϬϮϞϨϪϬ(χ₇: List[T]) -> List[T]:
        if len(χ₇) <= 1:
            return χ₇
        γΞψ𝖓 = χ₇[0]
        ₣ἆḞḜ₴ = [x for x in χ₇ if x < γΞψ𝖓]
        ɰΝϠȣ = [x for x in χ₇ if not (x < γΞψ𝖓) or (x == γΞψ𝖓 and x != χ₇[0])]
        return _ʭϞϽϰϚϢϬϮϞϨϪϬ(₣ἆḞḜ₴) + [γΞψ𝖓] + _ʭϞϽϰϚϢϬϮϞϨϪϬ(ɰΝϠȣ)

    œՓպ𐍈𐐘𐐙𐐚ϝⵏϚϡ = _ʭϞϽϰϚϢϬϮϞϨϪϬ(ΘΩΛΞψσ)

    ύϛϯϟχώϝ = 0
    ζὬᾓᾐᾑ = len(list_input)
    while ύϛϯϟχώϝ < ζὬᾓᾐᾑ:
        if (ύϛϯϟχώϝ % 3) == 0:
            list_input[ύϛϯϟχώϝ] = œՓպ𐍈𐐘𐐙𐐚ϝⵏϚϡ[int(ύϛϯϟχώϝ / 3)]
        ύϛϯϟχώϝ += 1

    return list_input