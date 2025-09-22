def CalculateGroups(TotalItems, GroupSize):
    q, r = divmod(TotalItems, GroupSize)
    if r > 0:
        return r * (q + 1)
    else:
        return TotalItems

# Main Program Logic
input_line = input()
TotalItemsA, TotalItemsB, GroupSize = map(int, input_line.split())

GroupsA = CalculateGroups(TotalItemsA, GroupSize)
GroupsB = CalculateGroups(TotalItemsB, GroupSize)

FinalResult = GroupsA * GroupsB
print(FinalResult)
