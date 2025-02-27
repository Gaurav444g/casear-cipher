def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters remain unchanged
    
    return result

# User interaction
if __name__ == "__main__":
    while True:
        message = input("Enter the message: ")
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").strip().lower()
        
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice! Please enter either 'encrypt' or 'decrypt'.")
            continue
        
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher(message, shift, choice)
        print(f"Result: {result}")
        
        another = input("Do you want to process another message? (yes/no): ").strip().lower()
        if another != 'yes':
            break
