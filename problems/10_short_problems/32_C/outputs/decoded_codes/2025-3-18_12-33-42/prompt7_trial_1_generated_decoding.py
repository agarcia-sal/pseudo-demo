def calculateTotalPages(totalItems, itemsPerPage):
    # Calculate quotient and remainder when totalItems is divided by itemsPerPage
    quotient = totalItems // itemsPerPage
    remainder = totalItems % itemsPerPage
    
    # If there's a remainder, we need an additional page for those leftover items
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return totalItems  # If no remainder, just return the original totalItems


def main():
    # Read totalItems, additionalItems, and itemsPerPage from input
    totalItems = int(input())
    additionalItems = int(input())
    itemsPerPage = int(input())
    
    # Calculate pages required for total items and additional items
    pagesForTotalItems = calculateTotalPages(totalItems, itemsPerPage)
    pagesForAdditionalItems = calculateTotalPages(additionalItems, itemsPerPage)
    
    # Print the product of pages required for total and additional items
    print(pagesForTotalItems * pagesForAdditionalItems)


# Run the main function to execute the program
if __name__ == "__main__":
    main()
