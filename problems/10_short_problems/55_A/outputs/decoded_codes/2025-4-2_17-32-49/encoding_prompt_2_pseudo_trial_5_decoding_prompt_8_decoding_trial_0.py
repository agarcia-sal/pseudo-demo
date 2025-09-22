# Start

# Input Requirement
totalElements = int(input())

# Initialize
isActive = [True] * totalElements
index = 0
step = 1

# Loop
while step <= 500000:
    if isActive[index]:
        isActive[index] = False
    step += 1
    index = (index + step) % totalElements

# Filter Active Elements
activeElements = [e for e in isActive if e]

# Output Requirement
if len(activeElements) == 0:
    print("YES")
else:
    print("NO")

# End
