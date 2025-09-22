def do_main():
    # Read input values
    input1 = input()
    input2 = input()

    # Split input strings into lists
    list1 = input1.split()
    list2 = input2.split()

    # Initialize the result counter
    mismatch_count = 0

    # Compare corresponding elements in both lists
    for index in range(3):
        value1 = int(list1[index])
        value2 = int(list2[index])

        if value1 != value2:
            mismatch_count += 1

    # Determine if the number of mismatches is less than 3
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")


# Main entry point
if __name__ == "__main__":
    do_main()
