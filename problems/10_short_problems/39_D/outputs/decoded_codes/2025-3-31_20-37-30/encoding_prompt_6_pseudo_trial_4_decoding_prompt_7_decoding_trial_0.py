def main():
    # Step 1: Get two lines of input from the user
    firstString = input()
    secondString = input()

    # Step 2: Split the input strings into lists of numbers
    firstList = firstString.split()
    secondList = secondString.split()

    # Step 3: Initialize a counter to track differences
    differenceCount = 0 

    # Step 4: Compare the numbers in each list
    for index in range(3):  # Loop until index 2
        firstNumber = int(firstList[index])  # Convert first number to integer
        secondNumber = int(secondList[index])  # Convert second number to integer
        
        # Step 5: Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment difference count if they're different

    # Step 6: Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
