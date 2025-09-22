def do_main():
    # Step 1: Take two inputs
    input1 = input()  # User input for first set of numbers
    input2 = input()  # User input for second set of numbers

    # Step 2: Split inputs into lists of strings
    list1 = input1.split()  # Split first input into a list of strings
    list2 = input2.split()  # Split second input into a list of strings

    # Step 3: Initialize a result counter
    result_counter = 0  # Counter to track differences

    # Step 4: Loop through the first three elements of the lists
    for index in range(3):
        # Convert string elements to integers
        number1 = int(list1[index])  # Convert to integer
        number2 = int(list2[index])  # Convert to integer
        
        # Step 5: Compare the numbers and update the counter
        if number1 != number2:  # Check if numbers are not equal
            result_counter += 1  # Increment counter if they are different

    # Step 6: Check the result counter
    if result_counter < 3:  # If differences are less than 3
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO"

# Step 7: Execute the do_main function if this script is run as the main program
if __name__ == "__main__":
    do_main()  # Call the main function
