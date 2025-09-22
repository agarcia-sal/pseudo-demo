def compare_value_sets():
    # Step 2: Receive Input
    first_set = input()
    second_set = input()

    # Step 3: Process Input
    first_values = first_set.split()
    second_values = second_set.split()

    # Step 4: Initialize Difference Counter
    difference_count = 0

    # Step 5: Compare Values
    for index in range(3):  # Loop from 0 to 2
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        if first_value != second_value:
            difference_count += 1

    # Step 6: Determine Result
    if difference_count < 3:
        print("YES")  # Sets differ in fewer than three positions
    else:
        print("NO")  # Sets differ in three or more positions

# Entry point of the program
if __name__ == "__main__":
    compare_value_sets()
