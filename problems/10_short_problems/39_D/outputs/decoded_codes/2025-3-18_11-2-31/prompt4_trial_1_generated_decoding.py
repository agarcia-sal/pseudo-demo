def main():
    # Initialize variables
    t1 = input()  # Get the first line of input
    t2 = input()  # Get the second line of input

    # Split the input strings into lists of strings
    tt1 = t1.split()  # Split by whitespace into a list
    tt2 = t2.split()  # Split by whitespace into a list

    # Initialize the difference counter
    res = 0

    # Compare the corresponding elements of the two lists
    for x in range(3):  # Loop through the first three elements
        # Convert the current elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # If the numbers are different, increment the difference counter
        if a != b:
            res += 1

    # Output result based on the number of differences
    if res < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
main()


    1 2 3
    1 2 4
    

    1 2 3
    4 5 6
    