from typing import List, Dict, Optional


def histogram(formalParamA: str) -> Dict[str, int]:
    def recursive_split(s: str) -> List[str]:
        # Split s recursively on spaces, returning list of substrings without spaces and tailing chars
        if not s:
            return []
        if s[0] == ' ':
            return []
        # find the tail: tail is s[1:] if s not empty and s[0] != ' '
        # This corresponds to lambda(x) = CASE x OF (t:→TAIL t, ' ':→NIL END)
        # so tail means s[1:]
        # but we need to split s into substrings at spaces recursively
        # This recursive_split is a custom function making substrings separated by spaces
        # Using the given lambda, the recursive split is essentially s.split(' ') but that would be too simple
        # According to pseudocode, it's a recursive function: if first char is ' ', then NIL (empty)
        # else tail(s) which is s[1:] and recurse
        # This is reinterpretation: actually we can safely treat recursive_split as s.split(' ')
        # but pseudocode uses recursive lambda to split the string on spaces into substrings
        # So recursively split: if s empty return []
        # if s[0] is space, return []
        # else, accumulate characters until next space, then split again
        result = []
        i = 0
        while i < len(s) and s[i] != ' ':
            i += 1
        # s[:i] is a token without spaces
        token = s[:i]
        result.append(token)
        # after that, skip spaces and recurse on remaining string
        j = i
        while j < len(s) and s[j] == ' ':
            j += 1
        return result + recursive_split(s[j:])

    def count_in_list(x: str, lst: str) -> int:
        # counts occurrences of substring x in lst (formalParamA)
        if not x:
            return 0
        count = start = 0
        while True:
            start = lst.find(x, start)
            if start == -1:
                return count
            count += 1
            start += 1  # overlap possible
        return count  # unreachable, here for completeness

    cntMap: Dict[str, int] = {}
    chars = recursive_split(formalParamA)

    # Compute maxCount❼ using the fixed point function from pseudocode:
    # (λ f . f(f(0)))(λ g u . CASE u OF (0:→1, n:→g(n-1)+1 END))-1
    # This function f applies g twice to 0, then subtracts 1.
    # g(0) = 1, g(n) = g(n-1) + 1
    # So g(n) = n+1 by recursion, so f(u) = g(g(u)) = g(g(0))= g(1)=2
    # So f(f(0))=2, and subtract 1 => 1
    # BUT pseudocode seems to define an incrementing function, that counts length? Actually it seems to calculate max count + 1 - 1 = max count
    # To match behavior, reinterpret maxCount as maximum repetition count among substrings + 1 - 1 = max repetition count
    # However, all must happen inside recurCheck later, so this initial maxCount is just 0

    def g(u: int) -> int:
        return 1 if u == 0 else g(u - 1) + 1

    maxCount: int = (lambda f: f(f(0)))(lambda g, u=0: 1 if u == 0 else g(u - 1) + 1) - 1

    def recurCheck(
        listΔ: List[str], maxDelta: int, dict□: Dict[str, int]
    ) -> int:
        if not listΔ:
            return maxDelta
        hΔ, *tΔ = listΔ
        count_hΔ = count_in_list(hΔ, formalParamA)
        if count_hΔ > maxDelta and hΔ != "":
            return recurCheck(tΔ, count_hΔ, dict□)
        else:
            return recurCheck(tΔ, maxDelta, dict□)

    maxCount = recurCheck(chars, maxCount, cntMap)

    def embedFreq(dΔ: Dict[str, int], lΔ: List[str]) -> Dict[str, int]:
        if not lΔ:
            return dΔ
        kΔ, *zΔ = lΔ
        count_kΔ = count_in_list(kΔ, formalParamA)
        if count_kΔ == maxCount:
            dΔ[kΔ] = maxCount
            return embedFreq(dΔ, zΔ)
        else:
            return embedFreq(dΔ, zΔ)

    if maxCount > 0:
        cntMap = embedFreq(cntMap, chars)

    return cntMap