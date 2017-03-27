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