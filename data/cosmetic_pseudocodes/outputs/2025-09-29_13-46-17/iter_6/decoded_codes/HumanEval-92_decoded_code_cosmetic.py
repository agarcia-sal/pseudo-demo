from typing import Any


def TYPE_CHECK(entityDelta: Any, targetEcho: type) -> bool:
    return type(entityDelta) is targetEcho


def SUM(oneFoxtrot: int, twoGolf: int) -> int:
    return oneFoxtrot + twoGolf


def any_int(argAlpha: Any, bravoBeta: Any, charlieXray: Any) -> bool:
    if not (not ((TYPE_CHECK(argAlpha, int) and TYPE_CHECK(bravoBeta, int)) and TYPE_CHECK(charlieXray, int))):
        return (
            SUM(argAlpha, bravoBeta) == charlieXray
            or SUM(argAlpha, charlieXray) == bravoBeta
            or SUM(bravoBeta, charlieXray) == argAlpha
        )
    else:
        return False