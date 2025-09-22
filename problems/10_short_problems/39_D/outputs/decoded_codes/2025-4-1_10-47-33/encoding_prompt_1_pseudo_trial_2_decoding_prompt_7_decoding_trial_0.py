def main():
    # Read input values from the user
    userInput1 = input()
    userInput2 = input()
    
    # Split the input strings into lists of strings
    list1 = userInput1.split()
    list2 = userInput2.split()
    
    # Initialize a counter for the differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert current elements to integers
        valueFromList1 = int(list1[index])
        valueFromList2 = int(list2[index])
        
        # Check if the values are different
        if valueFromList1 != valueFromList2:
            # Increment the difference counter
            differenceCount += 1 

    # Evaluate the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
