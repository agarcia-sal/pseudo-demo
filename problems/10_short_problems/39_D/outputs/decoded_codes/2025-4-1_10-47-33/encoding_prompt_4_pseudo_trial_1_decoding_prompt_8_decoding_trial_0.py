def main():
    # Read input values
    t1 = input()
    t2 = input()

    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize difference counter
    differenceCount = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert string values to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Count differences
        if a != b:
            differenceCount += 1

    # Determine output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute main function
main()
