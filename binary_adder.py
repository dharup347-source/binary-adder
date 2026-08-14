"""
Binary Adder
A beginner project for Electronics & VLSI students.
"""

def is_binary(number):
    """Check if the given string is a valid binary number."""
    for digit in number:
        if digit not in ("0", "1"):
            return False
    return True


def binary_add(bin1, bin2):
    """Add two binary numbers and return the binary result."""
    # Convert binary to decimal
    dec1 = int(bin1, 2)
    dec2 = int(bin2, 2)

    # Add the decimal values
    total = dec1 + dec2

    # Convert the sum back to binary
    binary_result = bin(total)[2:]

    return binary_result, total


def main():
    print("=" * 40)
    print("         BINARY ADDER")
    print("=" * 40)

    while True:
        bin1 = input("\nEnter first binary number (or 'quit' to exit): ").strip()

        if bin1.lower() == "quit":
            print("Goodbye!")
            break

        bin2 = input("Enter second binary number: ").strip()

        # Validate inputs
        if not is_binary(bin1) or not is_binary(bin2):
            print("Error: Please enter valid binary numbers (only 0 and 1).")
            continue

        if bin1 == "" or bin2 == "":
            print("Error: Input cannot be empty.")
            continue

        binary_result, decimal_result = binary_add(bin1, bin2)

        print("\n----------------------------")
        print(f"First Binary  : {bin1}")
        print(f"Second Binary : {bin2}")
        print(f"Binary Result : {binary_result}")
        print(f"Decimal Result: {decimal_result}")
        print("----------------------------")


if __name__ == "__main__":
    main()
