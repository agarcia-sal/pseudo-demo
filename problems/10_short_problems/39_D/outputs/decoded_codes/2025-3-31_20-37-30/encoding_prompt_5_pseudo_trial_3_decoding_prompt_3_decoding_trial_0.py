def main():
    # Step 1: Accept user input
    input1 = input()  # Prompt for first set of three numbers
    input2 = input()  # Prompt for second set of three numbers

    # Step 2: Split the inputs into individual numbers
    numbers1 = input1.split()  # Split the first input into a list of numbers
    numbers2 = input2.split()  # Split the second input into a list of numbers

    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter to track the number of differences

    # Step 4: Compare the corresponding values in both lists
    for index in range(3):
        value1 = numbers1[index]  # Get the value from the first list
        value2 = numbers2[index]  # Get the value from the second list

        # Step 5: Check if the numbers differ
        if value1 != value2:
            difference_count += 1  # Increment the counter if values differ

    # Step 6: Determine the output based on differences
    if difference_count < 3:
        print("YES")  # Print "YES" if differences are fewer than three
    else:
        print("NO")   # Print "NO" otherwise

# Step 7: Call the main function to execute the program
if __name__ == "__main__":
    main()
