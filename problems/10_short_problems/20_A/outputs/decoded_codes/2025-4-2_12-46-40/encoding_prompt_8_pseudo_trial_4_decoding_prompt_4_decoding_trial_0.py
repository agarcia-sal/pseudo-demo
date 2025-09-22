import re

def main():
    # Read the input from standard input and strip whitespace
    input_path = input().strip()

    # Remove unnecessary leading slashes, ensuring at most one leading slash
    normalized_path = re.sub(r'^/+','/', input_path)  # Replace multiple leading slashes with a single one
    
    # Print the normalized path to output
    print(normalized_path)

# Start execution by calling the main function
if __name__ == "__main__":
    main()
