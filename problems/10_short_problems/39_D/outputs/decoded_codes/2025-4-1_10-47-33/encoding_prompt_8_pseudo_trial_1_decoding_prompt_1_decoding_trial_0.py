def main():
    # Step 1: Read two lines of input from the user
    firstLine = input()
    secondLine = input()
    
    # Step 2: Split the input lines into lists of strings
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Loop through the first three elements of each list
    for index in range(3):
        # Convert strings to integers
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # Step 5: Compare numbers and count differences
        if firstNumber != secondNumber:
            differenceCount += 1
    
    # Step 6: Check if the number of differences is less than three
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Call the main function to execute the program
main()
