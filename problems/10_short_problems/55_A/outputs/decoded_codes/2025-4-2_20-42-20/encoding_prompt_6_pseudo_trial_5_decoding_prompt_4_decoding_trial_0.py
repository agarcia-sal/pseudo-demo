def main():
    # Input: Read integer n, representing the size of the array
    n = int(input())

    # Initialize an array 'isAlive' to track the status of each person
    isAlive = [True] * n
    currentIndex = 0
    stepCount = 1

    # Elimination process
    while stepCount <= 500000:
        if isAlive[currentIndex]:
            # Mark the current person as "eliminated"
            isAlive[currentIndex] = False

        # Increment step count
        stepCount += 1

        # Update current index, wrapping around if needed
        currentIndex = (currentIndex + stepCount) % n

    # Create a list of remaining "alive" persons
    remaining = [alive for alive in isAlive if alive]

    # Output result based on the remaining array
    if len(remaining) == 0:
        print("YES")  # No one is alive
    else:
        print("NO")   # There are still people alive

# Entry point of the program
if __name__ == "__main__":
    main()
