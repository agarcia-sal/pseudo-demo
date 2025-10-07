coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
return sorted(coords, key=lambda c: (c[0], -c[1]))