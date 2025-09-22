# 1. Start Program

def main():
    # 2. Receive Input:
    firstSet = [int(input()), int(input()), int(input())]  # First set of numbers
    secondSet = [int(input()), int(input()), int(input())]  # Second set of numbers

    # 3. Initialize Difference Count:
    differenceCount = 0  # Count of differences

    # 4. Loop through the Sets:
    for index in range(3):  # Loop from 0 to 2
        # Compare numbers from both sets
        if firstSet[index] != secondSet[index]:  # Check if they are different
            differenceCount += 1  # Increase the difference count

    # 5. Check the Number of Differences:
    if differenceCount < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")   # 3 or more differences

# 6. End Program
# 7. Execution of Program:
main()  # Run the program
