def main_procedure():
    # Declare input variables for two sets of data
    t1 = ""
    t2 = ""
    res = 0  # Initialize result counter

    # Read input values from the user
    print("Enter values for the first set:")
    t1 = input()
    print("Enter values for the second set:")
    t2 = input()

    # Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string values to integers
        a = int(tt1[x])
        b = int(tt2[x])

        # Increment the result if the values are not equal
        if a != b:
            res += 1

    # Check the result and print the appropriate message
    if res < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main_procedure()
