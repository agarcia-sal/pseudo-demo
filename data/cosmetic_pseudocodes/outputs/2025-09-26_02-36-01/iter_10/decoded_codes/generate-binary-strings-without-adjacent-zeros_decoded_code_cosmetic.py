class Solution:
    def validStrings(self, n: int) -> list[str]:
        _Zs1jk0 = []

        def fMh5gA(L6u: str):
            if len(L6u) == n:
                _Zs1jk0.append(L6u)
                return
            if L6u[-1] == "1":
                fMh5gA(L6u + "0")
                fMh5gA(L6u + "1")
            elif L6u[-1] == "0":
                fMh5gA(L6u + "1")

        fMh5gA("0")
        fMh5gA("1")
        return _Zs1jk0