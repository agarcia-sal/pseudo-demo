def main():
    # Step 1: Receive input
    firstSet = input()  # Prompt user for the first set of three numbers
    secondSet = input()  # Prompt user for the second set of three numbers

    # Step 2: Split the input strings into lists
    numbersFromFirstSet = firstSet.split()  # Split the first set input
    numbersFromSecondSet = secondSet.split()  # Split the second set input

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare the numbers in both sets
    for index in range(3):  # Loop through each index from 0 to 2
        numberFromFirst = int(numbersFromFirstSet[index])  # Convert to integer
        numberFromSecond = int(numbersFromSecondSet[index])  # Convert to integer

        # Step 5: Check if the numbers are different
        if numberFromFirst != numberFromSecond:
            differenceCount += 1  # Increment counter by 1 if numbers are different

    # Step 6: Evaluate the number of differences
    if differenceCount < 3:
        print("YES")  # Print YES if differences are less than 3
    else:
        print("NO")  # Print NO otherwise

# Step 7: Execute the main function
main()
