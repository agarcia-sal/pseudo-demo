def main():
    # Read two lines of input
    input1 = input()
    input2 = input()

    # Split the input strings into lists of values
    list1 = input1.split()
    list2 = input2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements from the lists to integers
        value1 = int(list1[index])
        value2 = int(list2[index])

        # Check if the values are different
        if value1 != value2:
            # Increment the difference count
            difference_count += 1
            
    # If the number of differences is less than 3, output "YES"
    if difference_count < 3:
        print("YES")
    else:
        # Otherwise, output "NO"
        print("NO")

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
