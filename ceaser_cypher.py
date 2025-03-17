from caeser_art import logo

print(logo)


alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caeser(original_text, shift_number, encode_or_decode):
    cipher_word = ""
    if encode_or_decode == "decode":
        shift_number *= -1
    for letter in original_text:
        if letter in alphabets:
            encoded_letter = alphabets[(alphabets.index(letter) + shift_number) % len(alphabets)]
            cipher_word += encoded_letter
        else:
            cipher_word += letter
        
    print(f"Here is the {encode_or_decode}d result: {cipher_word}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'. \n").lower()
    if restart == "no":
        print("Good Bye!")
        break