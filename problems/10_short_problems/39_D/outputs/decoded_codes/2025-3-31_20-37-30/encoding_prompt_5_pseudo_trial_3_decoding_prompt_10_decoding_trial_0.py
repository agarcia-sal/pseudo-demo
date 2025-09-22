def main():
    # Step 1: Accept user input
    input1 = input()
    input2 = input()

    # Step 2: Split the inputs into individual numbers
    numbers1 = input1.split()  # Splitting the first input into a list of numbers
    numbers2 = input2.split()  # Splitting the second input into a list of numbers

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare the corresponding values in both lists
    for index in range(3):  # Looping through indices 0, 1, and 2
        value1 = numbers1[index]  # Getting value from the first list
        value2 = numbers2[index]  # Getting value from the second list

        # Step 5: Check if the numbers differ
        if value1 != value2:
            difference_count += 1  # Increment the counter if values differ

    # Step 6: Determine the output based on differences
    if difference_count < 3:
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")   # Output NO otherwise

# Step 7: Call the main function to execute the program
if __name__ == "__main__":
    main()
