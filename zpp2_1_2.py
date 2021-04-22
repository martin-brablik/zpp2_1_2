def square_string(string):
    """Pokusí se převést textový řetězec na číslo a vrátit jeho druhou mocninu jako textový řetězec"""
    try:
        value = int(string)
        square = value * value
        return str(square) + '\n'
    except:
        raise RuntimeError("Hodnotu se nepodařilo převést na číslo")

def open_file(path, mode):
    """Pokusí se otevřít soubor"""
    try:
        return open(path, mode)
    except:
        raise RuntimeError("Nepodařilo se otevřít soubor " + path)

def file_number_map_square(input_path, output_path):
    """Pro soubor čísel vytvoří soubor jeho druhých mocnin"""
    input_file = open_file(input_path, 'r')
    try:
        output_file = open_file(output_path, 'w')
        line = input_file.readline()
        try:
            while line != '':
                output_file.write(square_string(line))
                line = input_file.readline()
        finally:
            output_file.close()
    finally:
        input_file.close()

input_path = input("Zadejte jméno vstupního souboru: ")
output_path = input("Zadejte jméno výstupního souboru: ")
try:
    file_number_map_square(input_path, output_path)
except RuntimeError as e:
    print("Chyba: \n", e)
else:
    print("Program byl úspěšně dokončen.")
