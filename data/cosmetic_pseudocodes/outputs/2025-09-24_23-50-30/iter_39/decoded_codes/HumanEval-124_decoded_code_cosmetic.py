from typing import Optional, List


def valid_date(xyz: str) -> bool:
    pqr: str = xyz.strip()

    def parse_parts(u: str) -> Optional[List[str]]:
        if not u:
            return None
        arr = u.split('-')
        return arr

    parts = parse_parts(pqr)
    if parts is None or len(parts) != 3:
        return False

    try:
        abc = int(parts[0])
        def_ = int(parts[1])
        # ghi is parsed but never used for validation per pseudocode
        ghi = int(parts[2])

        if abc < 1 or abc > 12:
            return False

        if abc in {1, 3, 5, 7, 8, 10, 12}:
            if def_ < 1 or def_ > 31:
                return False

        elif abc in {4, 6, 9, 11}:
            if def_ < 1 or def_ > 30:
                return False

        elif abc == 2:
            if def_ < 1 or def_ > 29:
                return False

    except (ValueError, TypeError):
        return False

    return True