def do_main():
    # Get user inputs as strings
    t1 = input()
    t2 = input()

    # Split input strings into lists of strings
    tt1 = t1.split()  # Split t1 into an array of strings
    tt2 = t2.split()  # Split t2 into an array of strings

    # Initialize result counter
    res = 0

    # Compare corresponding elements from both lists
    for x in range(3):  # Loop through indices 0 to 2
        a = int(tt1[x])  # Convert string to integer
        b = int(tt2[x])  # Convert string to integer
        if a != b:  # Check if the integers are different
            res += 1  # Increment the mismatch counter

    # Check the mismatch count to determine the output
    if res < 3:
        print("YES")  # Output if mismatches are less than 3
    else:
        print("NO")  # Output if mismatches are 3 or more

# Entry point for the program
if __name__ == "__main__":
    do_main()  # Call the main function
