def print_formatted(number):

    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Format: d=decimal, o=octal, X=hex(caps), b=binary
        # Use rjust(width) or format specifiers for space-padding
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        
        print(f"{decimal} {octal} {hexadecimal} {binary}")

