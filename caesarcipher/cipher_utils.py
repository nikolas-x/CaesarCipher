def translation_table_to_string(table):
    translations = []
    for k,v in table.items():
        translations.append(chr(k) + " => " + chr(v))
    return translations


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


def count_shifts(table):
    shiftmap = {}
    for k,v in table.items():
        shift = abs(int(k) - int(v))
        if shift in shiftmap:
            shiftmap[shift] += 1
        else:
            shiftmap[shift] = 1
    return shiftmap


# Generates a table containing each letter of the alphabet shifted by the given shift value
def build_translation_table(shift):
    key = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_list = list(alphabet)

    for i in range(0,26):
        key.append(alphabet[(i + shift) % 26])

    return str.maketrans(alphabet, ''.join(key))


# Translates a line with the given translation table
def translate(table, line):
    return line.upper().translate(table)

