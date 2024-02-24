def caesar(start_text, shift_amount, cipher_direction, alphabet="abcdefghijklmnopqrstuvwxyz"):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char.lower() in alphabet:
            position = alphabet.index(char.lower())
            new_position = (position + shift_amount) % len(alphabet)
            if char.isupper():
                end_text += alphabet[new_position].upper()
            else:
                end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid direction. Please choose 'encode' or 'decode'.")
        continue
    text = input("Type your message:\n")
    shift_input = input("Type the shift number:\n")
    
    try:
        shift = int(shift_input) % 26
    except ValueError:
        print("Invalid shift number. Please enter an integer.")
        continue

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Type 'no' otherwise.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
