userInput = abs(int(input()))


index = 0


while True:


    sum = (index * (index + 1)) // 2  # Using integer division since sum is an integer


    difference = sum - userInput


    if sum == userInput:
        print(index)
        break  # End the program


    elif sum > userInput:


        if difference % 2 == 0:
            print(index)
            break  # End the program


    index += 1


userInput = abs(int(input()))
index = 0

while True:
    sum = (index * (index + 1)) // 2
    difference = sum - userInput
    
    if sum == userInput:
        print(index)
        break
    elif sum > userInput:
        if difference % 2 == 0:
            print(index)
            break
            
    index += 1
