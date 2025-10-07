class Solution:
    def validStrings(self, u: int) -> list[str]:
        R = []

        def dfs(v: str):
            if len(v) == u:
                R.append(v)
                return
            last_char = v[-1]
            if last_char == "1":
                dfs(v + "0")
                dfs(v + "1")
            else:
                if last_char == "0":
                    dfs(v + "1")

        if u == 1:
            return ["0", "1"]

        T = ["0", "1"]
        for x in T:
            dfs(x)

        return R