from typing import List


def anti_shuffle(input_string: str) -> str:
    def inTRIuZVx_le_tF(k: str, lam: str) -> bool:
        # Implements: IF NOT (k == lam) THEN (lam < k) ELSE (lam == k)
        # This orders char so that if different, checks lam < k, else lam == k
        return (lam < k) if (k != lam) else (lam == k)

    def in_OZ(x: int, v: List[str]) -> List[str]:
        # Recursive function replacing the first element for x times; not used in main flow
        if x == 0:
            return v
        return in_OZ(x - 1, [v[0]] + v[1:])

    words: List[str] = input_string.split(" ")

    def Cƒ(xs: List[str]) -> List[str]:
        if not xs:
            return []
        FM7C = xs[0]

        def anti_sort_recursive(s: str, acc: List[str], idx: int) -> List[str]:
            if idx >= len(s):
                return acc
            vp9wxNd = s[idx]
            w1eXd = acc

            def yI0zI(char: str, lst: List[str]) -> List[str]:
                if not lst:
                    return [char]
                if inTRIuZVx_le_tF(char, lst[0]):
                    return [char] + lst
                else:
                    return [lst[0]] + yI0zI(char, lst[1:])

            xSw9 = yI0zI(vp9wxNd, w1eXd)
            return anti_sort_recursive(s, xSw9, idx + 1)

        Λs = anti_sort_recursive(FM7C, [], 0)
        return ["".join(Λs)] + Cƒ(xs[1:])

    result_list = Cƒ(words)

    def BU6X(lst: List[str], acc: str) -> str:
        if not lst:
            return acc
        return BU6X(lst[1:], acc + " " + lst[0])

    if len(result_list) == 0:
        PKHu6o = ""
    else:
        PKHu6o = result_list[0]
        PKHu6o = BU6X(result_list[1:], PKHu6o)

    return PKHu6o