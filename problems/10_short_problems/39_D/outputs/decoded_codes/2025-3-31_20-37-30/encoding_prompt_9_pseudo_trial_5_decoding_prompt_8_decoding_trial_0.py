# Start the program.

# Receive Input
firstSet = input()
secondSet = input()

# Process Input
firstNumbers = firstSet.split()
secondNumbers = secondSet.split()

# Initialize Differences Counter
differenceCount = 0

# Compare Numbers
for i in range(3):  # Looping over three positions
    firstNumber = int(firstNumbers[i])
    secondNumber = int(secondNumbers[i])
    if firstNumber != secondNumber:
        differenceCount += 1

# Determine Output
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End the program.


def compare_sets():
    while True:
        try:
            firstSet = input()
            secondSet = input()

            firstNumbers = list(map(int, firstSet.split()))
            secondNumbers = list(map(int, secondSet.split()))

            if len(firstNumbers) != 3 or len(secondNumbers) != 3:
                raise ValueError

            differenceCount = sum(1 for i in range(3) if firstNumbers[i] != secondNumbers[i])

            print("YES" if differenceCount < 3 else "NO")
            break
        except ValueError:
            print("Please enter exactly three numeric values for each set.")

compare_sets()
