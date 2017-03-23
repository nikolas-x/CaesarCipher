import sys


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

    combinedText = '\n'.join(text)
    charmap = count_chars(combinedText)
    print(combinedText)
    print(charmap)


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

if __name__ == "__main__":
    main()
