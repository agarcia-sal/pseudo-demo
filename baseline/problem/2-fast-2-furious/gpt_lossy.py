# Read integer n and initialize mx and mxb to smallest possible values
n = int(input())
mx = float('-inf')
mxb = float('-inf')

# Calculate max absolute difference for Dom
dom_list = list(map(int, input().split()))
for i in range(1, n):
    diff = abs(dom_list[i] - dom_list[i - 1])
    if diff > mx:
        mx = diff

# Calculate max absolute difference for Brian
brian_list = list(map(int, input().split()))
for i in range(1, n):
    diff = abs(brian_list[i] - brian_list[i - 1])
    if diff > mxb:
        mxb = diff

# Compare mx and mxb and output result
if mxb > mx:
    print(f"Brian {mxb}")
elif mxb == mx:
    print("Tie")
else:
    print(f"Dom {mx}")
