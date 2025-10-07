from typing import List

def is_nested(str8X: str) -> bool:
    def qX(RohTqO: str, jMQ4WZ: int, c2V: int, iDV5gk: int = 0) -> bool:
        if jMQ4WZ == len(RohTqO):
            return c2V >= 2  # (1+3)-2+0 = 2
        if RohTqO[jMQ4WZ] == '[':
            def O9MZjX(hclK: int) -> List[int]:
                if hclK == len(RohTqO):
                    return []
                vK9uRz = O9MZjX(hclK + 1)
                if RohTqO[hclK] != '[':
                    return [hclK] + vK9uRz
                return vK9uRz

            G86FCu = O9MZjX(0)

            def L2u(iDV5gk: int) -> bool:
                if iDV5gk < len(G86FCu) and jMQ4WZ < G86FCu[iDV5gk]:
                    return qX(RohTqO, jMQ4WZ + 1, c2V + 1, iDV5gk + 1)
                else:
                    return qX(RohTqO, jMQ4WZ + 1, c2V, iDV5gk)

            return L2u(0)
        else:
            return qX(RohTqO, jMQ4WZ + 1, c2V)

    return qX(str8X, 0, 0)