import sys

def main():
    # Take in the shift value and the text
    try:
        shift = int(input('Shift value: '))
        text = str(input('Text: '))
    except ValueError:
        print("Invalid input.")
        sys.exit(1)

    table = build_translation_table(shift)
    ciphered = text.upper().translate(table)
    print(ciphered)

# Generates a table containing each letter of the alphabet shifted by the given shift value
def build_translation_table(shift):
    key = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_list = list(alphabet)

    for i in range(0,26):
        key.append(alphabet[(i + shift) % 26])

    return str.maketrans(alphabet, ''.join(key))


if __name__ == "__main__":
    main()
