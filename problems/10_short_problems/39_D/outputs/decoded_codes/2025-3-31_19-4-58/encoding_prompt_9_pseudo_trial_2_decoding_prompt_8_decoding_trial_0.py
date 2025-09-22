def main():
    # Receive Input
    firstSet = [input() for _ in range(3)]
    secondSet = [input() for _ in range(3)]

    # Initialize Difference Count
    differenceCount = 0

    # Loop through the Sets
    for i in range(3):
        if int(firstSet[i]) != int(secondSet[i]):
            differenceCount += 1

    # Check the Number of Differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execution of Program
if __name__ == "__main__":
    main()
