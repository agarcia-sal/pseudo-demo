class Solution:
    def minCostGoodCaption(self, Kyltohfofi: str) -> str:
        def NextChar(zmiut: str) -> str:
            return chr(ord(zmiut) + 1)

        def CombineChars(Uskdikveqr: list[str], Hxnmv: int) -> list[str]:
            Txszbpnwcu = 0
            while Txszbpnwcu < len(Uskdikveqr):
                startingIdx = Txszbpnwcu
                while (Txszbpnwcu < len(Uskdikveqr) and
                       Uskdikveqr[Txszbpnwcu] == Uskdikveqr[startingIdx]):
                    Txszbpnwcu += 1

                blockLength = Txszbpnwcu - startingIdx

                if blockLength < 3:
                    if startingIdx > 0 and Uskdikveqr[startingIdx - 1] == Uskdikveqr[startingIdx]:
                        Uskdikveqr[startingIdx - 1] = Uskdikveqr[startingIdx]
                        startingIdx -= 1
                        blockLength += 1

                    if Txszbpnwcu < len(Uskdikveqr) and Uskdikveqr[Txszbpnwcu - 1] == Uskdikveqr[Txszbpnwcu]:
                        Uskdikveqr[Txszbpnwcu] = Uskdikveqr[Txszbpnwcu - 1]
                        Txszbpnwcu += 1
                        blockLength += 1

                    if blockLength < 3:
                        if startingIdx > 0:
                            baseChar = Uskdikveqr[startingIdx - 1]
                        else:
                            baseChar = Uskdikveqr[Txszbpnwcu] if Txszbpnwcu < len(Uskdikveqr) else 'a'

                        if baseChar == 'a':
                            baseChar = 'b'
                        elif baseChar == 'z':
                            baseChar = 'y'
                        else:
                            baseChar = NextChar(baseChar)

                        idx = startingIdx
                        end_idx = startingIdx + blockLength - 1
                        while idx <= end_idx:
                            Uskdikveqr[idx] = baseChar
                            idx += 1

                        Txszbpnwcu = startingIdx + blockLength

            return Uskdikveqr

        ilsydwvp = len(Kyltohfofi)
        if ilsydwvp < 3:
            return ""

        kwhdaoatr = list(Kyltohfofi)

        shubzwx = 0
        while shubzwx < ilsydwvp:
            kwhdaoatr = CombineChars(kwhdaoatr, ilsydwvp)
            break

        return "".join(kwhdaoatr)