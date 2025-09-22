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
    for index in range(3):  # iterate over indices 0 to 2
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Step 5: Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1 

    # Step 6: Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()
