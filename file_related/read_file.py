def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            cont = file.read()
        print(f"Content of the file '{file_name}' is:\n")
        print(cont)
    except Exception as e:
        print(f"Error: {e}")

file_name = "sampel.txt"

read_file(file_name)
