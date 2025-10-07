def histogram(s):
    letters = s.split(" ")
    counts = {l: letters.count(l) for l in letters if l != ""}
    if not counts:
        return {}
    max_count = max(counts.values())
    return {l: max_count for l, c in counts.items() if c == max_count}