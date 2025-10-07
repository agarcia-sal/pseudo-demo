class Solution:
    def validStrings(self, u: int) -> list[str]:
        if u == 1:
            return ["0", "1"]

        xo = []

        def probe(v: str) -> None:
            while True:
                if len(v) == u:
                    xo.append(v)
                    break

                if v[-1] == "1":
                    probe(v + "0")
                    probe(v + "1")
                    return
                else:  # v[-1] == "0"
                    probe(v + "1")
                    return

        probe("0")
        probe("1")
        return xo