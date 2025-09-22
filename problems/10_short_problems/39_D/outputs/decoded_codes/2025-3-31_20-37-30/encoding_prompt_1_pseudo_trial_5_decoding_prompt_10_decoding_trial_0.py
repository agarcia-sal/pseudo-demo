def doMain():
    # Read input for the first sequence of values
    input1 = input()
    # Read input for the second sequence of values
    input2 = input()

    # Split the inputs into lists of strings
    values1 = input1.split()
    values2 = input2.split()

    # Initialize a counter for differences
    difference_count = 0

    # Iterate through the indices 0 to 2 (inclusive)
    for i in range(3):
        # Convert the corresponding values to integers
        value1 = int(values1[i])
        value2 = int(values2[i])
        
        # Check if the values are different
        if value1 != value2:
            difference_count += 1

    # Check the count of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function if the script is executed directly
if __name__ == "__main__":
    doMain()
