def main():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input strings into lists of strings
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):  # iterating from 0 to 2
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values from both lists are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 
    
    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function
main()


    1 2 3 
    1 2 3
    

    1 2 3 
    4 5 6
    

    5 6 7 
    5 6 8
    

    1 2 
    1 3
    