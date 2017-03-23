import sys


def main():
    # Take in the shift value and the text
    try:
        shift = int(input('Shift value: '))
        print("Text (type ENDTEXT at the end of the text): ")
        text = []

        # We take in an array of text lines
        # We ignore newlines and break when the user types 'ENDTEXT'
        while True:
            try:
                line = sys.stdin.readline()
            except KeyboardInterrupt:
                break

            if not line:
                break

            if line == '\n':
                continue

            line = line.rstrip()

            if line.upper() == 'ENDTEXT':
                break

            text.append(line)
    except ValueError:
        print("Invalid input.")
        sys.exit(1)

    table = build_translation_table(shift)
    ciphered = [cipher(table, line) for line in text]
    print(*ciphered, sep='\n')


# Generates a table containing each letter of the alphabet shifted by the given shift value
def build_translation_table(shift):
    key = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_list = list(alphabet)

    for i in range(0,26):
        key.append(alphabet[(i + shift) % 26])

    return str.maketrans(alphabet, ''.join(key))


# Ciphers a line with the given translation table
def cipher(table, line):
    return line.upper().translate(table)


if __name__ == "__main__":
    main()
