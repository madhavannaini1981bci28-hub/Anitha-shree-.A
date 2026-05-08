rows = 5
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    
    print() # Move to the next line after each row
