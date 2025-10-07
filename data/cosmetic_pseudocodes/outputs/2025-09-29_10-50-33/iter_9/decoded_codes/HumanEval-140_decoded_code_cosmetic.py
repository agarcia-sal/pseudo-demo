from typing import List


def fix_spaces(text: str) -> str:
    result: List[str] = []
    offset: int = 0
    spaces_start: int = 0
    spaces_end: int = 0

    def _fix_spaces() -> None:
        nonlocal offset, spaces_start, spaces_end
        if offset < len(text):
            if text[offset] == " ":
                spaces_end += 1
            if text[offset] != " ":
                span = spaces_end - spaces_start
                if span > 2:
                    result.append("-")
                    result.append(text[offset])
                elif span > 0:
                    result.append("_" * span)
                    result.append(text[offset])
                else:
                    result.append(text[offset])
                spaces_start, spaces_end = offset + 1, offset + 1
            offset += 1
            _fix_spaces()
        else:
            span = spaces_end - spaces_start
            if span > 2:
                result.append("-")
            elif span > 0:
                result.append("_")

    _fix_spaces()
    return "".join(result)