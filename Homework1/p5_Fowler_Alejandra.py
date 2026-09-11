def caesar_cipher(text, shift):
    result = ""

    for letter in text:
        if "a" <= letter <= "z":
            result = result + chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        elif 'A' <= letter <= 'Z':
            result = result + chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        else:
            result = result + letter
    return result
    


def caesar_decipher(cyphertext, shift):
    return caesar_cipher(cyphertext, -shift)

def letter_frequency(text):
    freq = {}
    for char in text:
        lower_char = char.lower()
        if 'a' <= lower_char <= 'z':
            if lower_char in freq:
                freq[lower_char] += 1
            else:
                freq[lower_char] = 1
    return freq

def main():
    text = input("Write a message: ")
    shift= int(input("Shift Value:")) 
    ciphered = caesar_cipher(text,shift=shift)
    print("Ciphered text:", ciphered) 
    freq = letter_frequency(text)
    print("Letter frequency:", freq)
    deciphered = caesar_decipher(ciphered, shift=shift)
    print("Deciphered text:", deciphered)

if __name__ == "__main__":
    main()