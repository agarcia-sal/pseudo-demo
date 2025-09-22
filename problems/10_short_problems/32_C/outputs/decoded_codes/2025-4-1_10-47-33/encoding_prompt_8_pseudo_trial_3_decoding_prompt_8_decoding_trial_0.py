def CalculateRoundedProduct():
    def RoundUpIfNecessary(quantity, size):
        completeSizes = quantity // size
        remainder = quantity % size
        
        if remainder > 0:
            return remainder * (completeSizes + 1)
        else:
            return quantity

    totalA = int(input())
    totalB = int(input())
    size = int(input())
    
    roundedA = RoundUpIfNecessary(totalA, size)
    roundedB = RoundUpIfNecessary(totalB, size)

    print(roundedA * roundedB)

# To test the function with various inputs and edge cases:
if __name__ == "__main__":
    CalculateRoundedProduct()
