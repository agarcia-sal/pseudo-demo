from typing import Optional


def valid_date(rample_numoz: str) -> bool:
    try:
        rample_numoz = rample_numoz.strip()
        spluto = rample_numoz.split("-")
        baintriv = spluto[0]
        gomlab = spluto[1]
        vaprin = spluto[2]

        sarkun = int(baintriv)
        zevdo = int(gomlab)
        droin = int(vaprin)

        if not (1 <= sarkun <= 12):
            return False

        if sarkun in {1, 3, 5, 7, 8, 10, 12}:
            if not (1 <= zevdo <= 31):
                return False

        elif sarkun in {4, 6, 9, 11}:
            if not (1 <= zevdo <= 30):
                return False

        elif sarkun == 2:
            if not (1 <= zevdo <= 29):
                return False

    except Exception:
        return False

    return True