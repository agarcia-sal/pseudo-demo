def do_main():
    # Initialize variables
    t1 = ""
    t2 = ""
    result_count = 0

    # Get user input for two strings
    print("Enter first input:")
    t1 = input()
    print("Enter second input:")
    t2 = input()

    # Split input strings into lists based on spaces
    list_t1 = t1.split()
    list_t2 = t2.split()

    # Ensure both lists have at least 3 elements
    if len(list_t1) < 3 or len(list_t2) < 3:
        print("Both inputs must contain at least three space-separated integers.")
        return

    # Compare the elements of each list
    for x in range(3):
        a = int(list_t1[x])  # Convert string to integer for list_t1
        b = int(list_t2[x])  # Convert string to integer for list_t2

        # Check if the elements at index x are not equal
        if a != b:
            result_count += 1  # Increment mismatch counter

    # Check the result and print appropriate output
    if result_count < 3:
        print("YES")
    else:
        print("NO")


# Main block to execute the function
if __name__ == "__main__":
    do_main()
