def main():
    # Step 1: Get two lines of input from the user
    firstString = input()  # User inputs the first string
    secondString = input()  # User inputs the second string

    # Step 2: Split the input strings into lists of numbers
    firstList = firstString.split()  # Split the first string into a list
    secondList = secondString.split()  # Split the second string into a list

    # Step 3: Initialize a counter to track differences
    differenceCount = 0 

    # Step 4: Compare the numbers in each list
    for index in range(3):  # Check only the first three indices (0, 1, 2)
        # Convert the current elements to integers
        firstNumber = int(firstList[index])  
        secondNumber = int(secondList[index])  
        
        # Step 5: Check if the numbers are different
        if firstNumber != secondNumber:  
            differenceCount += 1  # Increment the count if they are different

    # Step 6: Determine if the number of differences is less than 3
    if differenceCount < 3:  
        print("YES")  # Fewer than 3 differences
    else:  
        print("NO")   # 3 or more differences

# Start the program by calling the main function
main()
