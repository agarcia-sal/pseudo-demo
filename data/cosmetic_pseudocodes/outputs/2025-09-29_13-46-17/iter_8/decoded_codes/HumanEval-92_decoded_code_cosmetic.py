from typing import Any

def any_int(x: Any, y: Any, z: Any) -> bool:
    def qx9g(p0ujr: int, lqp6t: int, rnvdl: int) -> bool:
        return p0ujr + lqp6t == rnvdl

    def cpf83(rdt48: Any, qgbej: Any, ifc0h: Any) -> bool:
        if not isinstance(rdt48, int):
            return False
        if not isinstance(qgbej, int):
            return False
        if not isinstance(ifc0h, int):
            return False
        return (
            qx9g(rdt48, qgbej, ifc0h)
            or qx9g(rdt48, ifc0h, qgbej)
            or qx9g(qgbej, ifc0h, rdt48)
        )

    return cpf83(x, y, z)