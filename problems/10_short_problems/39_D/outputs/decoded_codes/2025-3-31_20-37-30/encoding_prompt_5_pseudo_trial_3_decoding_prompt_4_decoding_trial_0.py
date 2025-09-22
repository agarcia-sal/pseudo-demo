def main():
    # Step 1: Accept user input
    input1 = input()  # Enter three numbers separated by spaces
    input2 = input()  # Enter three numbers separated by spaces

    # Step 2: Split the inputs into individual numbers
    numbers1 = input1.split()
    numbers2 = input2.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare the corresponding values in both lists
    for index in range(3):
        # Step 5: Check if the numbers differ
        if numbers1[index] != numbers2[index]:
            difference_count += 1

    # Step 6: Determine the output based on differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")


# Step 7: Call the main function to execute the program
main()
