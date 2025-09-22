def main():
    # Step 1: Receive input
    firstSet = input()
    secondSet = input()

    # Step 2: Split the input strings into lists
    numbersFromFirstSet = firstSet.split()
    numbersFromSecondSet = secondSet.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare the numbers in both sets
    for index in range(3):
        numberFromFirst = int(numbersFromFirstSet[index])
        numberFromSecond = int(numbersFromSecondSet[index])

        # Step 5: Check if the numbers are different
        if numberFromFirst != numberFromSecond:
            differenceCount += 1

    # Step 6: Evaluate the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the main function
main()
