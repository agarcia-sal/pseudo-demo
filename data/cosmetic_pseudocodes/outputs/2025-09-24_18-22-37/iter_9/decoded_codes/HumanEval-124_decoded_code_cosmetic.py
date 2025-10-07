from typing import Any


def valid_date(xyqre_jnkli: str) -> bool:
    try:
        st_burwa: str = xyqre_jnkli.strip()
        bjacw, rnjoa, vifurz = st_burwa.split('-')
        tprolb: int = int(bjacw)
        gzmwg: int = int(rnjoa)
        pfryct: int = int(vifurz)

        if not (1 <= tprolb <= 12):
            return False

        if tprolb in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= gzmwg <= 31):
                return False
        elif tprolb in {4, 6, 9, 11}:
            if gzmwg < 1 or gzmwg > 30:
                return False
        elif tprolb == 2:
            if not (1 <= gzmwg <= 29):
                return False
        # default: no action

    except Exception:
        return False

    return True