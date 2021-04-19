def write_to_file(filename, value, write_mode):
    try:
        file = open(filename, write_mode)
        file.write(value)
        file.close()
        return True
    except:
        print("Výstupní soubor se nepodařilo otevřít.")
        return False

def square_string(string):
    try:
        value = int(string)
        square = value * value
        return str(square) + '\n'
    except:
        print("\nHodnota na řádku nemohla být převedena na číslo.\nIgnorovat (1)\nPžeskočít (2)")
        option = int(input())
        if option == 1:
            return string
        else:
            return ''

def file_square(input_name, output_name):
    try:
        input_file = open(input_name)
        line = input_file.readline()
        if write_to_file(output_name, square_string(line), 'w'):
            line = input_file.readline()
            while line != "":
                write_to_file(output_name, square_string(line), 'a')
                line = input_file.readline()
        else:
            return
        input_file.close()
        print("Program byl úspěšně dokončen.")
    except:
        print("Vstupní soubor se nepodařilo otevřít.")

input_name = input("Zadejte jméno vstupního souboru: ")
output_name = input("Zadejte jméno výstupního souboru: ")
file_square(input_name, output_name)