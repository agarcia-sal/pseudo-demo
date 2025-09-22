def main():
    # Step 1: Accept two lines of input containing numbers
    first_line = input()
    second_line = input()
    
    # Step 2: Split the input strings into lists of numbers
    first_set = list(map(int, first_line.split()))
    second_set = list(map(int, second_line.split()))
    
    # Step 3: Initialize a counter for differing values
    difference_count = 0
    
    # Step 4: Compare each corresponding number from both sets
    for index in range(3):
        first_number = first_set[index]
        second_number = second_set[index]
        
        # If the numbers are different, increase the count
        if first_number != second_number:
            difference_count += 1
    
    # Step 5: Determine the output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Execute the main function if the script is run
if __name__ == "__main__":
    main()
