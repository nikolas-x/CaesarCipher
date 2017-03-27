import sys
import operator
from caesarcipher.cipher_utils import translation_table_to_string
from caesarcipher.cipher_utils import count_chars
from caesarcipher.cipher_utils import count_shifts
from caesarcipher.cipher_utils import build_translation_table
from caesarcipher.cipher_utils import translate


def main():
    # Take in the text
    try:
        print("Text (type ENDTEXT at the end of the text): ")
        text = []

        # We take in an array of text lines
        # We ignore newlines and break when the user types 'ENDTEXT'
        # TODO: Refactor repeated code to a class
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

    # Generate a string that represents the list of letters in decreasing order of frequency
    combinedText = '\n'.join(text)
    charmap = count_chars(combinedText)
    sorted_chars_expected = 'etaoinshrdlcumwfgypbvkjxqz'.upper() # English language letter frequency
    sorted_chars_actual = sorted(charmap.items(), key=operator.itemgetter(1), reverse=True)
    sorted_chars_actual = ''.join([tup[0] for tup in sorted_chars_actual])

    # Ensure both strings are of equal length
    # This helps deal with accented/missing letters
    # TODO: Treat accented letters as normal letters
    if (len(sorted_chars_actual) < len(sorted_chars_expected)):
        sorted_chars_actual += ('?' * (len(sorted_chars_expected) - len(sorted_chars_actual)))

    sorted_chars_actual = sorted_chars_actual[:len(sorted_chars_expected)]

    # Build translation table and translate text
    table = str.maketrans(sorted_chars_actual, sorted_chars_expected)
    print(*translation_table_to_string(table), sep='\n')
    deciphered = [translate(table, line) for line in text]
    print(*deciphered, sep='\n')


    # Attempt to decipher a Caesar cipher
    option = input("Attempt to decipher Caesar cipher? (Type 'YES' to confirm): ")
    if (option.upper() != "YES"):
        return

    shiftmap = count_shifts(table)
    expected_shift = max(shiftmap.items(), key=operator.itemgetter(1))[0]
    table = build_translation_table(-expected_shift)
    deciphered = [translate(table, line) for line in text]
    print(*deciphered, sep='\n')
    print("Shift estimate: ", expected_shift)


if __name__ == "__main__":
    main()
