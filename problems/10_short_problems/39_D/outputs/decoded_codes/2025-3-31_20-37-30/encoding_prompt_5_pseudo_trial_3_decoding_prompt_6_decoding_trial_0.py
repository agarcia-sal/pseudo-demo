def main():
    # Step 1: Accept user input
    input1 = input()  # User inputs three numbers separated by spaces
    input2 = input()  # User inputs another set of three numbers separated by spaces

    # Step 2: Split the inputs into individual numbers
    numbers1 = input1.split()  # Split first set of numbers into a list
    numbers2 = input2.split()  # Split second set of numbers into a list

    # Step 3: Initialize a counter for differences
    difference_count = 0  # Counter to track the number of differences

    # Step 4: Compare the corresponding values in both lists
    for index in range(3):  # Loop through index 0 to 2
        value1 = numbers1[index]  # Get value from the first list
        value2 = numbers2[index]  # Get value from the second list

        # Step 5: Check if the numbers differ
        if value1 != value2:
            difference_count += 1  # Increment the counter if numbers differ

    # Step 6: Determine the output based on differences
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" otherwise

# Step 7: Call the main function to execute the program
main()
