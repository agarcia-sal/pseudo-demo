n = int(input())

isAlive = [True] * n
currentIndex = 0
stepCount = 1

while stepCount <= 500000:
    if isAlive[currentIndex]:
        isAlive[currentIndex] = False  # Mark as eliminated
    stepCount += 1
    currentIndex = (currentIndex + stepCount) % n  # Wrap around if needed

remaining = [alive for alive in isAlive if alive]

if len(remaining) == 0:
    print("YES")  # No one is alive
else:
    print("NO")  # There are still people alive
