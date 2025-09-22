def main():
    # Step 2: Get an input value from the user and convert it to an absolute integer
    input_number = abs(int(input()))
    
    # Step 3: Initialize counter variable
    index = 0
    
    while True:
        # Step 4.1: Calculate the sum of integers from 0 to index
        sum_of_integers = (index * (index + 1)) // 2
        
        # Step 4.2: Calculate the difference
        difference = sum_of_integers - input_number
        
        # Step 4.3: Check if sum_of_integers equals input_number
        if sum_of_integers == input_number:
            print(index)
            break
        # Step 4.4: Check if sum_of_integers is greater than input_number
        elif sum_of_integers > input_number:
            # Step 4.4.1: Check if the difference is an even number
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 4.5: Increment index
        index += 1

# Step 1: Begin the program
if __name__ == "__main__":
    main()
