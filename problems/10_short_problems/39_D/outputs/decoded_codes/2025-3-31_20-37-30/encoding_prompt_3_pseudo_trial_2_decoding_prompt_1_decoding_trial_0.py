def main():
    # Step 1: Get input values
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare the corresponding elements of the two lists
    for index in range(3):
        firstElement = int(firstList[index])
        secondElement = int(secondList[index])
        
        # If elements are different, increment the counter
        if firstElement != secondElement:
            differenceCount += 1 

    # Step 5: Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Execute the main function if the program is run as main
if __name__ == "__main__":
    main()
