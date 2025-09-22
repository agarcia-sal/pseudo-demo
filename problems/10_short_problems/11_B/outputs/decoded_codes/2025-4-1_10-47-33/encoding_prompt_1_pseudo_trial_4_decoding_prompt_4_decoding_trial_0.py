def main():
    # Step 1: Get an input value from the user and convert it to an absolute integer
    inputNumber = abs(int(input()))
    
    # Step 2: Initialize a counter variable "index" to 0
    index = 0
    
    # Step 3: Start an infinite loop
    while True:
        # Step 4: Calculate the sum of all integers from 0 to "index"
        sumOfIntegers = (index * (index + 1)) // 2
        
        # Step 5: Calculate the difference
        difference = sumOfIntegers - inputNumber
        
        # Step 6: Check for equality
        if sumOfIntegers == inputNumber:
            print(index)
            break
        
        # Step 7: Check if the sum exceeds the input number
        if sumOfIntegers > inputNumber:
            # Step 8: Check if the difference is an even number
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 9: Increment "index" by 1
        index += 1

# Step 10: Call the main function to run the program
if __name__ == "__main__":
    main()
