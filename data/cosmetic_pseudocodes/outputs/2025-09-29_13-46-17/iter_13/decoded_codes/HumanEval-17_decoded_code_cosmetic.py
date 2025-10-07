from typing import List, Optional


def parse_music(music_string: str) -> List[int]:
    def ζρλ(ξ: str) -> int:
        if ξ == 'o':
            return 4
        elif ξ == 'o|':
            return 2
        elif ξ == '.|':
            return 1
        else:
            return 0

    def ζφωπ(mtstr: str, ψν: int) -> List[int]:
        if ψν >= len(mtstr):
            return []
        λετ = ""
        while ψν < len(mtstr) and mtstr[ψν] != ' ':
            λετ += mtstr[ψν]
            ψν += 1
        καμ: Optional[int] = ζρλ(λετ) if λετ != "" else None
        ινκ = ζφωπ(mtstr, ψν + 1)
        return [καμ] + ινκ if καμ is not None else ινκ

    return ζφωπ(music_string, 0)