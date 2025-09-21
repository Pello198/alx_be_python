# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to handle columns
    for col in range(size):
        print("*", end="")  # Print star without newline
    print()  # Newline after each row
    row += 1
