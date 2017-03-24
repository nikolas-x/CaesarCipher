import sys
import operator


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
    table = str.maketrans(sorted_chars_expected, sorted_chars_actual)
    deciphered = [decipher(table, line) for line in text]
    print(*deciphered, sep='\n')


# Generate a map of character counts for alphabetic characters
def count_chars(text):
    text = text.upper()
    charmap = {}
    escape = False
    for c in text:
        if c == '\\':
            escape = True
            continue

        if escape:
            escape = False
            continue

        if c.isalpha():
            if c in charmap:
                charmap[c] += 1
            else:
                charmap[c] = 1

    return charmap


def decipher(table, line):
    return line.upper().translate(table)


if __name__ == "__main__":
    main()
