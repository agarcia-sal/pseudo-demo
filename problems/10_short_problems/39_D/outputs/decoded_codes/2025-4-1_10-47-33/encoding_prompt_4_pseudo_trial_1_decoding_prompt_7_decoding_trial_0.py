def main():
    # Read input values
    t1 = input()  # Input for the first string
    t2 = input()  # Input for the second string
    
    # Split the input strings into lists of words
    tt1 = t1.split()  # Split first string by spaces
    tt2 = t2.split()  # Split second string by spaces
    
    # Initialize difference counter
    differenceCount = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string values to integers
        a = int(tt1[index])  # Convert the element from tt1 to integer
        b = int(tt2[index])  # Convert the element from tt2 to integer
        
        # Count differences
        if a != b:  # Check if the values are not equal
            differenceCount += 1  # Increment counter if there's a difference

    # Determine output based on the number of differences
    if differenceCount < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" if differences are 3 or more

# Execute main function
main()
