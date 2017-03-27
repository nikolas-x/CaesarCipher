import sys
from caesarcipher.cipher_utils import translation_table_to_string
from caesarcipher.cipher_utils import count_chars
from caesarcipher.cipher_utils import build_translation_table
from caesarcipher.cipher_utils import translate

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

    #debug
    charmap = count_chars('\n'.join(text))
    print(charmap)

    table = build_translation_table(shift)
    print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(*translation_table_to_string(table), sep='\n')
    ciphered = [translate(table, line) for line in text]
    print(*ciphered, sep='\n')


if __name__ == "__main__":
    main()
