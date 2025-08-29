def encode(message, shift):
    """Encodes a message by shifting letters forward"""
    result = ""
    for char in message:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  
    return result

def decode(message, shift):
    """Decodes a message by shifting letters backward"""
    return encode(message, -shift) 

def main():
    while True:
        print("==== Secret Code Generator ====")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            msg = input("Enter message to encode: ")
            try:
                shift = int(input("Enter shift number: "))
                print("✅ Encoded Message:", encode(msg, shift))
            except ValueError:
                print("❌ Invalid shift! Please enter a number.\n")

        elif choice == "2":
            msg = input("Enter message to decode: ")
            try:
                shift = int(input("Enter shift number: "))
                print("✅ Decoded Message:", decode(msg, shift))
            except ValueError:
                print("❌ Invalid shift! Please enter a number.\n")

        elif choice == "3":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
