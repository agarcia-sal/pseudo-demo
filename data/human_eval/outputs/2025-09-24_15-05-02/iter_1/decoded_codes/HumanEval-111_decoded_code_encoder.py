def histogram(s):
    L = s.split(" ")
    counts = {x: L.count(x) for x in L if x != ""}
    if not counts:
        return {}
    t = max(counts.values())
    return {x: t for x in counts if counts[x] == t} if t > 0 else {}