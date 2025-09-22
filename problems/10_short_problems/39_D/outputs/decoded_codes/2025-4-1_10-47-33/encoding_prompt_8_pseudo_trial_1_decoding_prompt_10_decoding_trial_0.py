def main():
    # Step 1: Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Step 2: Split the input lines into lists of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Loop through the first three elements of each list
    for index in range(3):  # Looping from 0 to 2
        # Convert strings to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Step 5: Compare numbers and count differences
        if first_number != second_number:
            difference_count += 1

    # Step 6: Check if the number of differences is less than three
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Call the main function to execute the program
main()
