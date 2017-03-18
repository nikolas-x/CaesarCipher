import sys


def main():
    # Take in the shift value and the text
    try:
        shift = int(input('Shift value: '))
        text = str(input('Text: '))
    except ValueError:
        print("Invalid input.")
        sys.exit(1)

    # Debug
    table = build_translation_table(shift)
    print(table)

# Generates a table containing each letter of the alphabet shifted by the given shift value
def build_translation_table(shift):
    table = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_list = list(alphabet)

    for i in range(0,26):
        table.append(alphabet[(i + shift) % 26])

    return table


if __name__ == "__main__":
    main()
