def main():
    # Read input values
    first_string = input()
    second_string = input()

    # Split the input strings into lists
    list1 = first_string.split()
    list2 = second_string.split()
    
    # Initialize the result counter for differences
    difference_count = 0 

    # Compare the first three elements of both lists
    for index in range(3):  # Iterate over the first three indices
        a = int(list1[index])  # Convert to integer
        b = int(list2[index])  # Convert to integer
        if a != b:  # Check for differences
            difference_count += 1  # Increment the difference counter

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the script runs
if __name__ == "__main__":
    main()
