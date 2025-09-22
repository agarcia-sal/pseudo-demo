def main():
    # Step 1: Gather Input
    input1 = input()
    input2 = input()

    # Step 2: Split Inputs into Lists
    list1 = input1.split()
    list2 = input2.split()

    # Ensure both lists contain exactly 3 elements
    if len(list1) != 3 or len(list2) != 3:
        print("Invalid input: Both inputs must contain exactly 3 numbers.")
        return

    # Step 3: Initialize a Result Counter
    result_counter = 0

    # Step 4: Compare Elements of Both Lists
    for index in range(3):
        # Convert current elements to integers
        value_from_list1 = int(list1[index])
        value_from_list2 = int(list2[index])

        # Step 5: Check if the values are different
        if value_from_list1 != value_from_list2:
            result_counter += 1

    # Step 6: Determine the Result
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the Main Function
if __name__ == "__main__":
    main()
