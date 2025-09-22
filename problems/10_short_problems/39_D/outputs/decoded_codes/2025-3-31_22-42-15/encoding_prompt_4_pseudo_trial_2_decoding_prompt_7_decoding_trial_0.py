def doMain():
    # Read input values
    firstLine = input()  # Input for the first line
    secondLine = input()  # Input for the second line
    
    # Split input lines into lists of strings
    list1 = firstLine.split()  # Split the first line into a list
    list2 = secondLine.split()  # Split the second line into a list
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from 0 to 2 inclusive
        # Convert the string elements to integers
        valueA = int(list1[index])  # Convert element from the first list to integer
        valueB = int(list2[index])  # Convert element from the second list to integer
        
        # Check if values are different
        if valueA != valueB:  # Check for inequality
            # Increment the difference counter
            differenceCount += 1  # Increment difference count if values differ
    
    # Check the number of differences
    if differenceCount < 3:  # Compare the difference count with 3
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" if differences are 3 or more

# Main execution starts here
doMain()
