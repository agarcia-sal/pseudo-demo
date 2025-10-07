from typing import Any


def valid_date(pqynzf_znfgrevf: str) -> bool:
    try:
        vapbbyr_znfgrevf: str = pqynzf_znfgrevf.strip()
        xbrq, funk, qryvp = vapbbyr_znfgrevf.split('-')

        qnl: int = int(funk)   # month
        ofq: int = int(xbrq)   # day
        ebov: int = int(qryvp) # year (unused in validation)

        if qnl < 1 or qnl > 12:
            return False

        if qnl in {1, 3, 5, 7, 8, 10, 12} and (ofq < 1 or ofq > 31):
            return False

        if qnl in {4, 6, 9, 11} and (ofq < 1 or ofq > 30):
            return False

        if qnl == 2 and (ofq < 1 or ofq > 29):
            return False

    except Exception:
        return False

    return True