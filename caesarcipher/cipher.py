import sys

def main():

    try:
        shift = int(input('Shift value: '))
        text = str(input('Text: '))
    except ValueError:
        print("Invalid input.")
        sys.exit(1)

    # Debug
    print("Shift: " + str(shift))
    print("Text: " + text)

if __name__ == "__main__" : main()