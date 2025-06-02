# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for each row
while row < size:
    # Use a for loop to print stars in a row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after one row is done
    row += 1

